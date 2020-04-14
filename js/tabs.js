// LINK TO TABS
var origurl = window.location.href;
window.location.hash = "";
function hashchanged(e, url) {
  if (!url) {
    url = window.location.href;
  }
  if (url.indexOf("#") > 0){
  var activeTab = url.substring(url.indexOf("#") + 1);
    $('.nav[role="tablist"] a[href="#'+activeTab+'"]').tab('show');
  }
}
$(document).ready(() => {
  hashchanged(null, origurl);
  $('a[role="tab"]').on("click", function() {
    var url = window.location.href;
    var newUrl;
    const hash = $(this).attr("href");
      newUrl = url.split("#")[0] + hash;
    history.replaceState(null, null, newUrl);
  });
});
$(window).on('hashchange', hashchanged);
