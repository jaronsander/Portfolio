$(function () {
  $(".nav-link").removeClass("active");
  if($(".index")[0]){
    $(".ix").addClass("active")
  } else if ($(".project-index")[0]){
    $(".px").addClass("active")
  }
});