// LINK TO TABS
function hashchanged() {
  var url = window.location.href;
  if (url.indexOf("#") > 0){
  var activeTab = url.substring(url.indexOf("#") + 1);
    $('.nav[role="tablist"] a[href="#'+activeTab+'"]').tab('show');
  }
}
$(document).ready(() => {
  hashchanged();
  var url = window.location.href;
  $('a[role="tab"]').on("click", function() {
    var newUrl;
    const hash = $(this).attr("href");
      newUrl = url.split("#")[0] + hash;
    history.replaceState(null, null, newUrl);
  });
});
$(window).on('hashchange', hashchanged);
