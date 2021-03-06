<!DOCTYPE html>
<html>
   <head>
     <title>Homepage of The Master</title>
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
     <link rel="stylesheet" href="static/css/styles.css">
     <script src="static/js/scripts.js"></script>
   </head>
   <body>
			<div class="navbar">
        <div class="header">
          <h3>VirtFinance</h3>
        </div>
        <a href="index.html" class="page-button">
					<div>
					Home
					</div>
				</a>
        <a href="https://github.com/efeemir103" class="icon">
          <div>
            <img src="https://avatars0.githubusercontent.com/u/28904269?s=40&amp;u=26cb24095d1880c0950256f6c27516247d9784e1&amp;v=4" alt="Profile photo of me">
            <br />
            Check me up @ Github
          </div>
        </a>
			</div>
      <hr style="clear:both;" />
			<div class="content">
				<div class="left-side">
          <button onclick="document.getElementById('id01').style.display='block'" style="width:auto;">Login</button>
          <div id="id01" class="modal">
            <form class="modal-content animate" action="#">
              <div class="container">
                <label for="uname"><b>Username</b></label>
                <input type="text" placeholder="Enter Username" name="uname" required>
                <label for="psw"><b>Password</b></label>
                <input type="password" placeholder="Enter Password" name="psw" required>
                <button type="submit">Login</button>
                <label>
                  <input type="checkbox" checked="checked" name="remember"> Remember me
                </label>
              </div>
              <div class="container" style="background-color:#f1f1f1">
                <button type="button" onclick="document.getElementById('id01').style.display='none'" class="cancelbtn">Cancel</button>
              </div>
            </form>
          </div>
			  </div>
				<div class="center">
					<div class="currency-catalog">
            % for currency_symbol, currency_name in curr_names.items():
              <a href="/rates/{{currency_symbol}}"><div class="currency-catalog-item">{{currency_name}} - {{currency_symbol}}</div></a>
            % end
          </div>
				</div>
				<div class="right-side">
				</div>
			</div>
			<div class="footer">
				<div class="about-creator">
					Made by Efe Emir Pekmez (2019)
				</div>
			</div>
   </body>
</html>
