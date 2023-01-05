function make_link(url) {
  if (url === '') {
    return '';
  }
  return "<a href=" + url + " onClick='openModal();' >Datasheet</a>";
}

function make_popup(wreck) {
  var usage_note = "<br>There is more information available at the following resources. Note: all data at the following links is from external sources, please refer to the linked sources for usage or reproduction constraints."
  var wh_link = make_link(wreck['wreckhunter_link']);
  var bl_link = make_link(wreck["beavertail_link"]);
  var name = "<strong>" + wreck["vessel_name"] + "</strong>";
  var year = ( wreck["year"] > 0 ) ? wreck["year"] : "";
  var msg_box = name;
  if (year !== "") {
    msg_box += "<br>Year Lost: " + year;
  }
  if (wh_link.length === 0 && bl_link.length === 0) {
    msg_box += "<br>No data or references available for this wreck...yet :)";
    return msg_box;
  }
  msg_box += usage_note
  msg_box += "<ul>";
  if (wh_link.length > 0) {
    msg_box += "<li>Wreck Hunter (<a href='http://wreckhunter.net/' target=\"_blank\" rel=\"noopener noreferrer\">Website</a>, " + wh_link + ")</li>"; 
  }
  if (bl_link.length > 0) {
    msg_box += "<li>Beavertail Lighthouse Museum (<a href='https://beavertaillight.org/wrecks/' target=\"_blank\" rel=\"noopener noreferrer\">Website</a>, " + bl_link + ")</li>";
  }
  msg_box += "</ul>";
  return msg_box;
}