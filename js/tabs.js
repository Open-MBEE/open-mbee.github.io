// LINK TO TABS
$(document).ready(() => {
  var url = window.location.href;
  if (url.indexOf("#") > 0){
  var activeTab = url.substring(url.indexOf("#") + 1);
    $('.nav[role="tablist"] a[href="#'+activeTab+'"]').tab('show');
  }

  $('a[role="tab"]').on("click", function() {
    var newUrl;
    const hash = $(this).attr("href");
      newUrl = url.split("#")[0] + hash;
    history.replaceState(null, null, newUrl);
  });
});
