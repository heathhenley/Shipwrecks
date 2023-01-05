    // Event handler to open modal / iframe for datasheet
    function openModal(elem) {
      // TODO (Heath): Does event.target.dataset work in all modern browsers?
      document.getElementById("popupdarkbg").style.display = "block";
      document.getElementById("popup").style.display = "block";
      document.getElementById('popupiframe').src = event.target.dataset["url"];
      document.getElementById('popupdarkbg').onclick = function() {
        document.getElementById("popup").style.display = "none";
        document.getElementById("popupdarkbg").style.display = "none";
        document.getElementById('popupiframe').src = "";
      };
      return false;
    }
    window.onkeydown = function(e) {
      if (e.keyCode == 27) {
        document.getElementById("popup").style.display = "none";
        document.getElementById("popupdarkbg").style.display = "none";
        e.preventDefault();
        return;
      }
    }