<template>
  <div>
    <Navbar/>
    <div style="margin-top:-20px;background-image: url(../assets/logo.png);background-size: 100% 100%; min-height: 800px; background-repeat: no-repeat;">
    <div class="title">Tour Guide</div>
    <div class="intro">Navigate the Road of Knowledge:</div>
    <div class="intro"> Your In-Car Companion for Instant Answers and Conversations.</div>
    <div style=" background-color: rgba(0, 0, 0, 0.4); background-size: contain; border-radius: 10px; width: 70%;margin-left: auto;margin-right: auto; margin-top: 20px; /* 圆角边框 */
">
    <div style="height: 10px"></div>
    <div class="input-container">
      <div>
        <!-- 按钮 -->
        <!-- <button @click="recOpen">Allow use microphone</button> -->

        <div class="container" >
        <button class="mic" @click="recStart">      
          <img src="../assets/mic.png" />
        </button>
        <div>
          <input type="text" class="custom-input" style="font-family: 'Calibri', Arial, sans-serif;  font-weight:bold;font-size: 16px;" placeholder="Search" v-model="inputText"/>
        </div>

      <button class= "search" @click="recStop">
          <img src="../assets/search-icon.png" />
        </button>
      </div>
        <!-- 波形绘制区域 -->
        <div class="wave">
          <div style="  background-color: rgb(0,0,0,0.2); border-radius: 10px;height: 130px; width: 570px; margin-left: auto;margin-right: auto;margin-bottom: 10px;" ref="recwave"></div>
        </div>
      </div>

  </div>
  <div v-show="loading" class="load" >Voice is wandering...</div>
  <div style="display: flex; justify-content: center;  margin-top:30px;">
  <div class="return_text" v-show="get_text">
  <div style="  font-family: 'Calibri', Arial, sans-serif;  font-weight:bold;margin: 15px; font-size:20px; background-color: #ffffff;" id="text" > </div>
  </div>
  <button style="width: 80px; height:80px;border-width: 0; background-color: rgba(126, 126, 126, 0);" v-if="get_audio" @click="playAudio">
    <img style="margin-left:-10px;max-width: 100%; max-height: 100%;" src="../assets/play.png" />
  </button>
</div>
<div style="height: 20px"></div>

</div>

</div>
</div>
    
</template>


<script>
import Navbar from './navbar.vue';
import Recorder from 'recorder-core';
import axios from 'axios';

//引入mp3格式支持文件；如果需要多个格式支持，把这些格式的编码引擎js文件放到后面统统引入进来即可
import 'recorder-core/src/engine/mp3';
import 'recorder-core/src/engine/mp3-engine';
//录制wav格式的用这一句就行
import 'recorder-core/src/engine/wav';

//可选的插件支持项，这个是波形可视化插件
import 'recorder-core/src/extensions/waveview';
//ts import 提示：npm包内已自带了.d.ts声明文件（不过是any类型）

let recBlob= null;
// const audioRecorder = new MicRecorder({ bitRate: 128 });

import AWS from 'aws-sdk';

AWS.config.update({
  accessKeyId: 'YOUR_ACCESS_KEY_ID',
  secretAccessKey: 'YOUR_SECRET_ACCESS_KEY',
  region: 'us-east-1'
});

const s3 = new AWS.S3();
export default {
    data() {
      return {
        rec: null,
        inputText: '' ,
        timestamp: '',
        get_audio: false,
        get_text: false,
        wave: null,
        intervalAudio: null,
        intervalText: null,
        loading: false
      };
    },
    components: {
        Navbar,
    },
    mounted() {
      // this.recOpen()
    },

    deactivated() {
      this.rec.close();
      this.rec = null;
      clearInterval(this.interval);
    },
    methods: {
      
      recOpen() {
        this.rec= Recorder({
          type: 'mp3', //录音格式，可以换成wav等其他格式
          sampleRate: 16000, //录音的采样率，越大细节越丰富越细腻
          bitRate: 16, //录音的比特率，越大音质越好
          onProcess: (
            buffers,
            powerLevel,
            bufferSampleRate,
          ) => {
            //录音实时回调，大约1秒调用12次本回调
            //可实时绘制波形，实时上传（发送）数据
            if (this.$refs.wave) {
              this.$refs.wave.input(buffers[buffers.length - 1], powerLevel, bufferSampleRate);
            }
          },
        })
        //创建录音对象
        if (!this.rec) {
          alert('当前浏览器不支持录音功能！');
          return;
        }
        //打开录音，获得权限
        this.rec.open(
          () => {
            console.log('录音已打开');
            if (this.$refs.recwave) {
              //创建音频可视化图形绘制对象
              this.$refs.wave = Recorder.WaveView({ elem: this.$refs.recwave });
            }
          },
          (msg, isUserNotAllow) => {
            //用户拒绝了录音权限，或者浏览器不支持录音
            console.log((isUserNotAllow ? 'UserNotAllow，' : '') + '无法录音:' + msg);
          },
        );
      },
      recStart() {
        this.recOpen()
        if (!this.rec) {
          console.error('未打开录音');
        }
        this.rec.start();
        console.log('已开始录音');
      },
      recStop() {
        if (this.inputText) {
          this.fetchData()
          return
        }
        if (!this.rec) {
          console.error('未打开录音');
          return;
        }
        this.rec.stop(
          (blob, duration) => {
            recBlob = blob;
            //简单利用URL生成本地文件地址，此地址只能本地使用，比如赋值给audio.src进行播放，赋值给a.href然后a.click()进行下载（a需提供download="xxx.mp3"属性）
            const localUrl = (window.URL || window.webkitURL).createObjectURL(blob);
            console.log('录音成功', blob, localUrl, '时长:' + duration + 'ms');
            this.upload(blob); //把blob文件上传到服务器
            this.rec.close(); //关闭录音，释放录音资源，当然可以不释放，后面可以连续调用start
            this.rec = null;
          },
          (err) => {
            console.error('结束录音出错：' + err);
            this.rec.close(); //关闭录音，释放录音资源，当然可以不释放，后面可以连续调用start
            this.rec = null;
          },
        );
      },
      playAudio() {
        this.audio.play();
      },

      upload(blob) {
        console.log(blob)
        const current_time = new Date();

        // 格式化时间为 ddmmyyHHMMSS 格式
        const timestamp = current_time.getDate().toString().padStart(2, '0') +
                          (current_time.getMonth() + 1).toString().padStart(2, '0') + // 月份从 0 开始
                          current_time.getFullYear().toString().substring(2) +
                          current_time.getHours().toString().padStart(2, '0') +
                          current_time.getMinutes().toString().padStart(2, '0') +
                          current_time.getSeconds().toString().padStart(2, '0');

        console.log(timestamp); 
        this.timestamp = timestamp
        const file_name = '0_'+ timestamp + '.mp3'
        const params = {
          Bucket: 'input-voice-store', // 替换为您的 S3 桶名
          Key: file_name, // 文件在 S3 中的路径
          Body: blob,
          ContentType: 'audio/mp3'
        };

        s3.upload(params, function(err, data) {
          if (err) {
            console.error('上传错误:', err);
          } else {
            console.log('上传成功:', data.Location);
          }
        });
        this.loading = true
        this.get_text = false
        this.get_audio = false
        this.intervalAudio = setInterval(this.checkAudioS3Updates, 2000);
        this.intervalText = setInterval(this.checkTextS3Updates, 2000);
      },
      
      recPlay() {
      const localUrl = URL.createObjectURL(recBlob);
      const audio = document.createElement('audio');
      audio.controls = true;
      document.body.appendChild(audio);
      audio.src = localUrl;
      audio.play(); //这样就能播放了
      //注意不用了时需要revokeObjectURL，否则霸占内存
      setTimeout(function () {
        URL.revokeObjectURL(audio.src);
      }, 5000);
    },

    fetchData() {
      const current_time = new Date();

      // 格式化时间为 ddmmyyHHMMSS 格式
      const timestamp = current_time.getDate().toString().padStart(2, '0') +
                        (current_time.getMonth() + 1).toString().padStart(2, '0') + // 月份从 0 开始
                        current_time.getFullYear().toString().substring(2) +
                        current_time.getHours().toString().padStart(2, '0') +
                        current_time.getMinutes().toString().padStart(2, '0') +
                        current_time.getSeconds().toString().padStart(2, '0');

      console.log(timestamp); 
      this.timestamp = timestamp
      const file_name = '0_'+ timestamp + '.txt'
      const blob = new Blob([this.inputText], { type: 'text/plain' });
      const params = {
        Bucket: 'input-text-store', // 替换为您的 S3 桶名
        Key: file_name, // 文件在 S3 中的路径
        Body: blob
      };

      s3.upload(params, function(err, data) {
        if (err) {
          console.error('上传错误:', err);
        } else {
          console.log('上传成功:', data.Location);
        }
      });
      this.inputText = ''
      this.loading = true
      this.get_text = false
      this.get_audio = false
      this.intervalAudio = setInterval(this.checkAudioS3Updates, 2000);
      this.intervalText = setInterval(this.checkTextS3Updates, 2000);
    },
    checkAudioS3Updates() {
      const file_name = '0_'+this.timestamp +'.mp3'
      // const file_name = 'file.mp3'
      axios.get('https://polly-voice-store.s3.amazonaws.com/'+file_name, {responseType: 'blob'})
        .then(response => {
          const url = URL.createObjectURL(response.data);
          const audio = new Audio(url);
          this.audio = audio
          this.get_audio = true
          this.loading = false
          clearInterval(this.intervalAudio);

        })
        .catch(error => {
          console.log('S3 请求失败:', error);
        });
    },
    checkTextS3Updates() {
      const file_name = '0_'+this.timestamp +'.txt'
      // const file_name = "file.txt"
      axios.get('https://output-text-store.s3.amazonaws.com/' + file_name, {responseType: 'blob'})
        .then(response => {
          console.log(3214134134)
          response.data.text().then(text => {
          console.log("文件内容:", text);
          this.get_text = true
          this.loading = false
          document.getElementById("text").innerText = text;
          clearInterval(this.intervalText);
        });
      })
        .catch(error => {
          console.log('S3 请求失败:', error);
        });
    },    
    }
}


</script>

<style>
.load {
  margin-top: 30px;
  font-family: 'Calibri', Arial, sans-serif;  
  font-weight:bold;
  font-size: 46px;
  color: #ffffff;
  text-align: center;
  padding-top: 10px;
}
.title {
  font-family: 'Calibri', Arial, sans-serif;  
  font-weight:bold;
  font-size: 46px;
  color: #ffffff;
  text-align: center;
  padding-top: 10px;
}
.intro {
  font-family: 'Calibri', Arial, sans-serif;  
  font-weight:bold;
  font-size: 26px;
  color: #ffffff;
  text-align: center;
  padding-top: 10px;
}

.input-container {
  /* background-color: rgb(182, 150, 216, 0.9);  */
  background-color: rgba(255, 255, 255, 0.4); 
  width:80%;
  margin-left: auto;
  margin-right: auto;
  border-radius: 10px; /* 圆角边框 */
  margin-top: 20px; /* 增加上边距，根据需要调整这个值 */


}
.container {
  margin-top: 30px;
  padding-top: 30px;
  display: flex;
  align-items: center; /* 垂直居中对齐 */
  justify-content: center; /* 水平居中 */

}
.custom-input {
  border: 3px solid #000000; /* 灰色边框 */
  border-radius: 10px; /* 圆角边框 */
  padding: 10px; /* 内边距 */
  width: 400px; /* 输入框宽度 */
  /* margin-top: 50px; */
  height: 50px; /* Adjust the height as needed */

}

.click-button {
  display: flex;
  justify-content: center;
  /* align-items: center; */
  margin-top: 50px;
  height: 140px; /* Adjust the height as needed */
}

.wave {
  display: inline-block; 
  padding: 10px;
  vertical-align: bottom;
  height:200%;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  margin-top:10px;

}
.mic {
  width: 80px; /* Adjust width as needed */
  height: 80px; /* Ensure it's the same as width for a square shape */
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  margin-right: 5px;
  cursor: pointer;
  background-color: rgb(182, 150, 216, 0.2);

}

.search {
  border-radius: 10px; /* 圆角边框 */
  width: 70px; /* Adjust width as needed */
  height: 70px; /* Ensure it's the same as width for a square shape */
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgb(182, 150, 216, 0.2);
  border: none;
  cursor: pointer;
  margin-left: 3px;
}

.search img {
  max-width: 100%; /* Adjust image size */
  max-height: 100%; /* Adjust image size */
  border-radius: 15px; /* Adjust border-radius for rounded corners */

}

.mic img {
  max-width: 100%; /* Adjust image size */
  max-height: 100%; /* Adjust image size */
  border-radius: 15px; /* Adjust border-radius for rounded corners */

}
.return_text {
  border-style: solid;
  border-radius: 8px;
  border-color: #000000;
  border-width: 3px; 
  height:200%;
  width: 75%;
  background-color: #ffffff;
  margin-left:2%
}
</style>