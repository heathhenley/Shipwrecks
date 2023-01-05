    // Event handler to open modal / iframe for datasheet
    function openModal() {
      // TODO (Heath): This is using the global window event, instead should add
      // a listener that takes a param to the link tags instead
      event.preventDefault();
      document.getElementById("popupdarkbg").style.display = "block";
      document.getElementById("popup").style.display = "block";
      document.getElementById('popupiframe').src = event.target["href"];
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