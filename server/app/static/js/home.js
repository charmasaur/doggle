function is_valid_guess(guess) {
    return guess in CHOICES;
}

window.onload = function() {
  twemoji.parse(document.body);
  var previous_guesses = [];

  var guess_form_element = document.getElementById("guess_form");
  var guess_element = document.getElementById("guess");
  var result = document.getElementById("result");

  guess_form_element.onsubmit = function() {
      var guess = guess_element.value;
      guess_element.value = "";
      if (previous_guesses.includes(guess) || !is_valid_guess(guess)) {
          return false;
      }
      previous_guesses.push(guess);

      var row = result.insertRow(-1);

      var cell;

      cell = row.insertCell(-1);
      cell.innerHTML = guess;

      cell = row.insertCell(-1);
      cell.innerHTML = CHOICES[guess]['similarity'];

      cell = row.insertCell(-1);
      cell.innerHTML = CHOICES[guess]['rank'] + "/" + Object.keys(CHOICES).length;

      if (CHOICES[guess]['rank'] == 1) {
          row.className = "success";
      }

      return false;
  };
}
