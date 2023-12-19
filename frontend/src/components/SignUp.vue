<template>
  <div id="content-container">
    <div id="_bg__sign_up_page"></div>
    <div id="frame">
      <div id="_bg__frame_ek1"></div>
      <div id="auto_layout_horizontal">
        <div id="_bg__auto_layout_horizontal_ek1"></div>
        <div id="wandervoice">WanderVoice</div>
      </div>

      <div id="auto_layout_vertical">
        <div id="_bg__auto_layout_vertical_ek1"></div>
        <div id="ellipse_4"></div>
        <img src="assets/voice_wave___dark.png" id="voice_wave___dark" />
        <div id="your_innovative_in_car_voice_assistant__experience_the_future_of_voice_assistants_in_your_car_">
          Your innovative in-car voice assistant. <br/><br/>Experience the future of voice assistants in your car!
        </div>
      </div>
    </div>

    <div id="ellipse_3"></div>

    <div id="frame_ek6">
      <div id="_bg__frame_ek7"></div>

      <!-- Already a member? Section -->
      <div id="auto_layout_horizontal_ek2">
		<div id="frame_ek8">
			<div id="_bg__auto_layout_horizontal_ek3"></div>
			<div id="already_a_member_">Already a member?
			<router-link id="_log_in_link" to="/login">Log In</router-link>
			</div>
		</div>


		<div id="_bg__frame_ek9"></div>
			<div id="sign_up_to_wandervoice">Sign up to<br/>WanderVoice</div>
			
			<!-- Name Field -->
			<div id="auto_layout_vertical_ek2">
			<div id="name">Name</div>
			<input type="text" id="name_input" placeholder="Enter your name">
			</div>
			
			<!-- Username Field -->
			<div id="auto_layout_vertical_ek4">
			<div id="username">Username</div>
			<input type="text" id="username_input" placeholder="Choose a username">
			</div>
			
			<!-- Email Field -->
			<div id="auto_layout_vertical_ek6">
			<div id="email">Email</div>
			<input type="email" id="email_input" placeholder="Enter your email">
			</div>
			
			<!-- Password Field -->
			<div id="auto_layout_vertical_ek8">
			<div id="password">Password</div>
			<input type="password" id="password_input" placeholder="Create a password">
			</div>
			
			<!-- Terms and Conditions Checkbox -->
			<div id="frame_ek18">
			<input type="checkbox" id="terms_checkbox">
			<label for="terms_checkbox" id="creating_an_account_means_you_re_okay_with_our_terms_of_service__privacy_policy__and_our_default_notification_settings_">
				Creating an account means you're okay with our Terms of Service, Privacy Policy, and our default Notification Settings.
			</label>
			</div>
			
			<!-- Create Account Button -->
			<router-link id="_log_in_link" to="/login">Create Account</router-link>

			<!-- reCAPTCHA Notice -->
			<div id="auto_layout_horizontal_ek18">
			<div id="_bg__auto_layout_horizontal_ek19"></div>
			<div id="this_site_is_protected_by_recaptcha_and_the_google_privacy_policy_and_terms_of_service_apply_">
				This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.
			</div>
		</div>
		</div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'SignUp',
  
};
</script>

<style scoped>
ody { margin: 0px; padding: 0px; font-family:"Arial"; overflow-x:hidden; }


img { position: absolute; display: block; margin: 0px; border: none; padding: 0px; }

div { position: absolute; }

#content-container { display: block; position: relative; width: 1511px; width: 1511px; height: 933px; overflow: hidden; display: block;  margin-left: auto; margin-right: auto;  }

#_bg__sign_up_page {
	top: 0px;
	left: 0px;
	width: 1511px;
	height: 933px;
	background:#;
}

#frame {
	top: 0px;
	left: 0px;
	width: 585px;
	height: 941px;
}

#_bg__frame_ek1 {
	top: 0px;
	left: 0px;
	width: 585px;
	height: 941px;
	background:rgba(192.88,145.27,222.06,1);
}

#auto_layout_horizontal {
	top: 338px;
	left: 166px;
	width: 286px;
	height: 48px;
}

#_bg__auto_layout_horizontal_ek1 {
	top: 0px;
	left: 0px;
	width: 286px;
	height: 48px;
	background:#;
}


#wandervoice {
	top: 1px;
	left: 21.17px;
	width: 237px;
	height: 59px;
	overflow: hidden;
	font-family: Abhaya Libre ExtraBold;
	font-size: 40px;
	line-height: 54px;
	text-align: center;
	letter-spacing: 0.25px;
	color:#FFFFFF;
}

#auto_layout_vertical {
	top: -14px;
	left: 35px;
	width: 479px;
	height: 911px;
}

#_bg__auto_layout_vertical_ek1 {
	top: 0px;
	left: 0px;
	width: 479px;
	height: 911px;
	background:#;
}


#ellipse_4 {
	top: 64px;
	left: 64px;
	width: 342px;
	height: 237px;
	-ms-border-radius: 171px / 118.5px;
	-o-border-radius: 171px / 118.5px;
	-moz-border-radius: 171px / 118.5px;
	-webkit-border-radius: 171px / 118.5px;
	border-radius: 171px / 118.5px;
	
	-ms-transform:rotate(-180deg);
	-o-transform:rotate(-180deg);
	-webkit-transform:rotate(-180deg);
	-moz-transform:rotate(-180deg);
	transform:rotate(-180deg);
	background:rgba(255,255,255,0);
	background: -webkit-radial-gradient(closest-side, rgba(137,0,255,1) 0%, rgba(255,216,186,1) 100%);
	background: -o-radial-gradient(closest-side, rgba(137,0,255,1) 0%, rgba(255,216,186,1) 100%);
	background: -moz-radial-gradient(closest-side, rgba(137,0,255,1) 0%, rgba(255,216,186,1) 100%);
	background: -ms-radial-gradient(closest-side, rgba(137,0,255,1) 0%, rgba(255,216,186,1) 100%);
	background: radial-gradient(closest-side, rgba(137,0,255,1) 0%, rgba(255,216,186,1) 100%);
}


#voice_wave___dark {
	top: 333px;
	left: 64px;
	width: 75px;
	height: 45px;
}


#your_innovative_in_car_voice_assistant__experience_the_future_of_voice_assistants_in_your_car_ {
	top: 394px;
	left: 64px;
	width: 336.2px;
	height: 275.2px;
	overflow: hidden;
	font-family: Abhaya Libre SemiBold;
	font-size: 32px;
	line-height: 270.2px;
	text-align: left;
	line-height: 38px;
	color:#866118;
}

#frame_ek2 {
	top: 708px;
	left: 64px;
	width: 90px;
	height: 22.5px;
}

#_bg__frame_ek3 {
	opacity:0.7;
	top: 0px;
	left: 0px;
	width: 90px;
	height: 22.5px;
	background:#;
}

#frame_ek4 {
	top: 0px;
	left: 0px;
	width: 90px;
	height: 22.5px;
}

#_bg__frame_ek5 {
	top: 0px;
	left: 0px;
	width: 90px;
	height: 22.5px;
	background:#;
}


#ellipse_3 {
	top: 725px;
	left: 0px;
	width: 278px;
	height: 208px;
	-ms-border-radius: 139px / 104px;
	-o-border-radius: 139px / 104px;
	-moz-border-radius: 139px / 104px;
	-webkit-border-radius: 139px / 104px;
	border-radius: 139px / 104px;
	background:rgba(255,255,255,0);
	background: -webkit-radial-gradient(closest-side, rgba(34,80,255,1) 0%, rgba(188.34,153,255,1) 100%);
	background: -o-radial-gradient(closest-side, rgba(34,80,255,1) 0%, rgba(188.34,153,255,1) 100%);
	background: -moz-radial-gradient(closest-side, rgba(34,80,255,1) 0%, rgba(188.34,153,255,1) 100%);
	background: -ms-radial-gradient(closest-side, rgba(34,80,255,1) 0%, rgba(188.34,153,255,1) 100%);
	background: radial-gradient(closest-side, rgba(34,80,255,1) 0%, rgba(188.34,153,255,1) 100%);
}

#frame_ek6 {
	top: 0px;
	left: 585px;
	width: 873px;
	height: 941px;
}

#_bg__frame_ek7 {
	top: 0px;
	left: 0px;
	width: 873px;
	height: 941px;
	background:rgba(246.37,246.37,246.37,1);
}

#auto_layout_horizontal_ek2 {
	top: 51px;
	left: -2px;
	width: 845px;
	height: 20px;
}

#_bg__auto_layout_horizontal_ek3 {
	top: 0px;
	left: 0px;
	width: 845px;
	height: 20px;
	background:#;
}


#already_a_member_ {
	top: 0px;
	left: 693.34px;
	width: 117.4px;
	height: 24.4px;
	overflow: hidden;
	font-family: Abhaya Libre;
	font-size: 14px;
	line-height: 19.4px;
	text-align: right;
	line-height: 20px;
	color:#000000;
}


#_log_in {
	top: 0px;
	left: 804.34px;
	width: 44.4px;
	height: 24.4px;
	overflow: hidden;
	font-family: Abhaya Libre;
	font-size: 14px;
	line-height: 19.4px;
	text-align: right;
	line-height: 20px;
	color:#4F3CC9;
}



#_bg__frame_ek9 {
	top: 0px;
	left: 0px;
	width: 536px;
	height: 747px;
	background:#;
}


#sign_up_to_wandervoice {
	top: 65.5px;
	left: 47px;
	width: 263.6px;
	height: 73.6px;
	overflow: hidden;
	font-family: Abhaya Libre SemiBold;
	font-size: 36px;
	line-height: 68.6px;
	text-align: left;
	line-height: 29px;
	padding-top: 7px;
	margin-top: -7px;
	color:#0D0C22;
}

#frame_ek10 {
	top: 190px;
	left: 60px;
	width: 416px;
	height: 557px;
}

#_bg__frame_ek11 {
	top: 0px;
	left: 0px;
	width: 416px;
	height: 557px;
	background:#;
}

#auto_layout_horizontal_ek4 {
	top: 0px;
	left: 0px;
	width: 416px;
	height: 106px;
}

#_bg__auto_layout_horizontal_ek5 {
	top: 0px;
	left: 0px;
	width: 416px;
	height: 106px;
	background:#;
}

#auto_layout_vertical_ek2 {
	top: 12px;
	left: 0px;
	width: 199.67px;
	height: 82px;
}

#_bg__auto_layout_vertical_ek3 {
	top: 0px;
	left: 0px;
	width: 199.67px;
	height: 82px;
	background:#;
}

#frame_ek8 {
  align-self: center;
  display: flex;
  flex-direction: column;
  height: 747px;
  margin-left: 1px;
  position: relative;
  width: 536px;
}

#name {
	top: 14px;
	left: 0px;
	width: 47.4px;
	height: 28.4px;
	overflow: hidden;
	font-family: Abhaya Libre SemiBold;
	font-size: 14px;
	line-height: 23.4px;
	text-align: left;
	line-height: 24px;
	margin-top: -3.3333333333333px;
	height: 42.4px;
	color:#0D0C22;
}

#frame_ek12 {
	top: 42px;
	left: 0px;
	width: 199.67px;
	height: 40px;
}

#_bg__frame_ek13 {
	top: -1px;
	left: -1px;
	width: 199.67px;
	height: 40px;
	-ms-border-radius: 8px;
	-o-border-radius: 8px;
	-moz-border-radius: 8px;
	-webkit-border-radius: 8px;
	border-radius: 8px;
	border: 1px solid #ea4c89;
	-ms-box-shadow:0px 0px 0px 1px rgba(234,76,137,0.1);
	-o-box-shadow:0px 0px 0px 1px rgba(234,76,137,0.1);
	-webkit-box-shadow:0px 0px 0px 1px rgba(234,76,137,0.1);
	-moz-box-shadow:0px 0px 0px 1px rgba(234,76,137,0.1);
	box-shadow:0px 0px 0px 1px rgba(234,76,137,0.1);
	background:rgba(255,255,255,1);
}

#auto_layout_vertical_ek4 {
	top: 12px;
	left: 216.33px;
	width: 199.67px;
	height: 82px;
}

#_bg__auto_layout_vertical_ek5 {
	top: 0px;
	left: 0px;
	width: 199.67px;
	height: 82px;
	background:#;
}


#username {
	top: 14px;
	left: 0px;
	width: 72.4px;
	height: 28.4px;
	overflow: hidden;
	font-family: Abhaya Libre SemiBold;
	font-size: 14px;
	line-height: 23.4px;
	text-align: left;
	line-height: 24px;
	margin-top: -3.3333333333333px;
	height: 42.4px;
	color:#0D0C22;
}

#frame_ek14 {
	top: 42px;
	left: 0px;
	width: 199.67px;
	height: 40px;
}

#_bg__frame_ek15 {
	top: 0px;
	left: 0px;
	width: 199.67px;
	height: 40px;
	-ms-border-radius: 8px;
	-o-border-radius: 8px;
	-moz-border-radius: 8px;
	-webkit-border-radius: 8px;
	border-radius: 8px;
	background:rgba(243,243,244,1);
}

#auto_layout_vertical_ek6 {
	top: 118px;
	left: 0px;
	width: 416px;
	height: 82px;
}

#_bg__auto_layout_vertical_ek7 {
	top: 0px;
	left: 0px;
	width: 416px;
	height: 82px;
	background:#;
}


#email {
	top: 14px;
	left: 0px;
	width: 50.5px;
	height: 28.5px;
	overflow: hidden;
	font-family: Abhaya Libre SemiBold;
	font-size: 15px;
	line-height: 23.5px;
	text-align: left;
	line-height: 24px;
	margin-top: -3px;
	height: 43.5px;
	color:#0D0C22;
}

#frame_ek16 {
	top: 42px;
	left: 0px;
	width: 416px;
	height: 40px;
}

#_bg__frame_ek17 {
	top: 0px;
	left: 0px;
	width: 416px;
	height: 40px;
	-ms-border-radius: 8px;
	-o-border-radius: 8px;
	-moz-border-radius: 8px;
	-webkit-border-radius: 8px;
	border-radius: 8px;
	background:rgba(243,243,244,1);
}

#auto_layout_horizontal_ek6 {
	top: 0px;
	left: 4px;
	width: 398px;
	height: 39px;
}

#_bg__auto_layout_horizontal_ek7 {
	top: 0px;
	left: 0px;
	width: 398px;
	height: 39px;
	-ms-border-radius: 8px;
	-o-border-radius: 8px;
	-moz-border-radius: 8px;
	-webkit-border-radius: 8px;
	border-radius: 8px;
	background:rgba(243,243,244,1);
}

#auto_layout_horizontal_ek8 {
	top: 12px;
	left: 17px;
	width: 364px;
	height: 15px;
}

#_bg__auto_layout_horizontal_ek9 {
	top: 0px;
	left: 0px;
	width: 364px;
	height: 15px;
	background:#;
}


#enter_email {
	top: 0px;
	left: 0px;
	width: 76.3px;
	height: 19.3px;
	overflow: hidden;
	font-family: Abhaya Libre;
	font-size: 13px;
	line-height: 14.3px;
	text-align: left;
	color:#9E9EA7;
}

#auto_layout_vertical_ek8 {
	top: 224px;
	left: 0px;
	width: 406px;
	height: 81px;
}

#_bg__auto_layout_vertical_ek9 {
	top: 0px;
	left: 0px;
	width: 406px;
	height: 81px;
	background:#;
}


#password {
	top: 14px;
	left: 0px;
	width: 74.5px;
	height: 28.5px;
	overflow: hidden;
	font-family: Abhaya Libre SemiBold;
	font-size: 15px;
	line-height: 23.5px;
	text-align: left;
	line-height: 24px;
	margin-top: -3px;
	height: 43.5px;
	color:#0D0C22;
}

#auto_layout_horizontal_ek10 {
	top: 42px;
	left: 0px;
	width: 406px;
	height: 39px;
}

#_bg__auto_layout_horizontal_ek11 {
	top: 0px;
	left: 0px;
	width: 406px;
	height: 39px;
	-ms-border-radius: 8px;
	-o-border-radius: 8px;
	-moz-border-radius: 8px;
	-webkit-border-radius: 8px;
	border-radius: 8px;
	background:rgba(243,243,244,1);
}

#auto_layout_horizontal_ek12 {
	top: 12px;
	left: 17px;
	width: 372px;
	height: 15px;
}

#_bg__auto_layout_horizontal_ek13 {
	top: 0px;
	left: 0px;
	width: 372px;
	height: 15px;
	background:#;
}


#_6__characters {
	top: 0px;
	left: 0px;
	width: 84.3px;
	height: 19.3px;
	overflow: hidden;
	font-family: Abhaya Libre;
	font-size: 13px;
	line-height: 14.3px;
	text-align: left;
	color:#9E9EA7;
}

#frame_ek18 {
	top: 330px;
	left: 0px;
	width: 416px;
	height: 36px;
}

#_bg__frame_ek19 {
	top: 0px;
	left: 0px;
	width: 416px;
	height: 36px;
	background:#;
}


#rectangle {
	top: -1px;
	left: -1px;
	width: 20px;
	height: 20px;
	border: 1px solid #dbdbde;
	background:rgba(255,255,255,1);
}

#auto_layout_horizontal_ek14 {
	top: 0px;
	left: 32px;
	width: 384px;
	height: 36px;
}

#_bg__auto_layout_horizontal_ek15 {
	top: 0px;
	left: 0px;
	width: 384px;
	height: 36px;
	background:#;
}


#creating_an_account_means_you_re_okay_with_our_terms_of_service__privacy_policy__and_our_default_notification_settings_ {
	top: 0px;
	left: 0px;
	width: 386.77px;
	height: 40.3px;
	overflow: hidden;
	font-family: Abhaya Libre;
	font-size: 13px;
	line-height: 35.3px;
	text-align: left;
	line-height: 18px;
	color:#6E6D7A;
}


#_bg___auto_layout_horizontal_ek17 {
	top: 0px;
	left: 0px;
	width: 188px;
	height: 40px;
	-ms-border-radius: 8px;
	-o-border-radius: 8px;
	-moz-border-radius: 8px;
	-webkit-border-radius: 8px;
	border-radius: 8px;
	background:rgba(234,76,137,1);
}


#create_account {
	top: 10px;
	left: 50.13px;
	width: 88.3px;
	height: 24.3px;
	overflow: hidden;
	font-family: Abhaya Libre Medium;
	font-size: 13px;
	line-height: 19.3px;
	text-align: center;
	line-height: 20px;
	margin-top: -2.3333333333333px;
	height: 37.3px;
	color:#FFFFFF;
}

#auto_layout_horizontal_ek18 {
	top: 460px;
	left: 0px;
	width: 300px;
	height: 32px;
}

#_bg__auto_layout_horizontal_ek19 {
	top: 0px;
	left: 0px;
	width: 300px;
	height: 32px;
	background:#;
}


#this_site_is_protected_by_recaptcha_and_the_google_privacy_policy_and_terms_of_service_apply_ {
	top: 0px;
	left: 0px;
	width: 310.05px;
	height: 35.1px;
	overflow: hidden;
	font-family: Abhaya Libre;
	font-size: 11px;
	line-height: 30.1px;
	text-align: left;
	line-height: 16px;
	color:#9E9EA7;
}
</style>