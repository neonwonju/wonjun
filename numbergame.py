<!DOCTYPE html>
<html>
<head>
	<title>숫자 맞추기 게임</title>
</head>
<body>
	<h1>숫자 맞추기 게임</h1>
	<p>1부터 100 사이의 숫자를 맞춰보세요.</p>
	<form>
		<label for="guess">숫자 입력:</label>
		<input type="number" id="guess" name="guess">
		<input type="button" value="확인" onclick="checkGuess()">
	</form>
	<p id="result"></p>
	<script>
		var answer = Math.floor(Math.random() * 100) + 1;
		var guessCount = 0;
		function checkGuess() {
			var guess = parseInt(document.getElementById("guess").value);
			guessCount++;
			if (guess === answer) {
				document.getElementById("result").innerHTML = "축하합니다! " + guessCount + "번 만에 맞추셨습니다.";
			} else if (guess < answer) {
				document.getElementById("result").innerHTML = "너무 작습니다.";
			} else {
				document.getElementById("result").innerHTML = "너무 큽니다.";
			}
		}
	</script>
</body>
</html>
