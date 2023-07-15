//  //to show nad hide modal
//  var elements = document.getElementsByClassName("buttn");
//  for (var i=0; i<elements.length; i++) {
//      elements[i].addEventListener("click", function() {
//          document.querySelector('.bg-modal').style.display = "flex";
//      });
//  }
//  // document.getElementsByClassName('buttn').addEventListener("click", function() {
//  //     document.querySelector('.bg-modal').style.display = "flex";
//  // });
 
//  document.querySelector('.close').addEventListener("click", function() {
//      document.querySelector('.bg-modal').style.display = "none";
//  });


 //for modal's data
 function orderModal(sid,url, country, language, DA, link_allowed, PA, description, organic_traffic){
     document.getElementById('url').href = document.getElementById('url').textContent = url;
    //  document.getElementById('url2').value =url;
     document.getElementById('url').textContent = url;
     document.getElementById('sid').value = sid;
     document.getElementById('country').textContent = country;
     document.getElementById('language').textContent = language;
     document.getElementById('link-allowed').textContent = link_allowed;
    //  document.getElementById('link').value = link_allowed;
     document.getElementById('mDA').textContent = DA;
    //  document.getElementById('DA').textContent = DA;
     document.getElementById('mPA').textContent = PA;
     document.getElementById('desc').textContent = description;
     document.getElementById('mtraffic').textContent = organic_traffic;
     $("#modal-contents").modal();
 }

 function orderModal2(sid){
     document.getElementById('sid2').value = sid;
     $("#modal-contents").modal();
 }
 
 
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}


var datefield = document.getElementById("datefield");
datefield.min = new Date().toISOString().split("T")[0];




// var button = document.getElementById('bpbutton'); // Assumes element with id='button'

  
  $(document).ready(function () {
    $("#bpbutton").click(function () {
        // $("#bp").toggle();
        var la = $('#link_allowed');
        var link = la.text();
        alert(link)
        // for (var i=1; i<=link;i++)
        //     $(".KUL").append('<div class="form-row"><div class="mb-2 col-lg-4 col-md-4"><input name="keyword'+i+'" class="input-form-v2 input-sm input-dashed form-control " type="text"placeholder="Keyword'+' '+i+'" value=""></div><div class="mb-2 col-lg-4 col-md-4"><input name="url'+i+'" autocomplete="off" class="input-form-v2 input-sm input-dashed form-control " type="url" placeholder="URL'+' '+i+'" value=""></div><div class="mb-2 col-lg-4 col-md-4"><select name="type_link_1" class="input-form-grey input-sm select-sm form-control" required=""><option value="">Link type</option><option value="0">Follow</option></select></div></div>');
    });
});

// $("bpbutton").click(function(){
//   alert("The paragraph was clicked.");
// });
// var la = $('#link_allowed');
//         var link = la.text();
//         for (var i=1; i<=link;i++)
//             $(".KUL").append('<div class="form-row"><div class="mb-2 col-lg-4 col-md-4"><input name="keyword'+i+'" class="input-form-v2 input-sm input-dashed form-control " type="text"placeholder="Keyword'+' '+i+'" value=""></div><div class="mb-2 col-lg-4 col-md-4"><input name="url'+i+'" autocomplete="off" class="input-form-v2 input-sm input-dashed form-control " type="url" placeholder="URL'+' '+i+'" value=""></div><div class="mb-2 col-lg-4 col-md-4"><select name="type_link_1" class="input-form-grey input-sm select-sm form-control" required=""><option value="">Link type</option><option value="0">Follow</option></select></div></div>');


      // $('#save_edit_info').click(function(){
      //     var medical_data1=$('#name').val();
      //     var hcc_data1 =$('#code').val();
      //     if(medical_data1 && hcc_data1)
      //     {
      //       $("#myModal").modal('hide');
             
      //       row_h.html(hcc_data1);
            
      //       row_m.html(medical_data1);
      //     }
      //     else
      //     {
      //         alert("fields required");
      //     }
      // });
   
      

    //   $(document).ready(function () {
    //     $("#atc").click(function () {
    //       // // content = 'hhelo'
    //       // var content = tinymce.get('mytextarea').getContent({ format:"text"});
    //       alert('clikced');
    //       // $("#tmc").text(content);
    //     });
    // });      

    //to show cart details
    function showcartdetails(current){
      // tinymce.activeEditor.setMode('readonly');
      $("#title").val($(current).closest('tr').children()[2].textContent);
      $("#limit_time").val($(current).closest('tr').children()[3].textContent);
      $("#linkkeywords").text($(current).closest('tr').children()[4].textContent);
      $("#linkurls").text ($(current).closest('tr').children()[5].textContent);
      $("#linktype").text($(current).closest('tr').children()[6].textContent);
      // tinymce.get('mytextarea').getBody().setAttribute('contenteditable', 'false');
      YourEditor.setData($(current).closest('tr').children()[7].textContent);
      // editor.data.set($(current).closest('tr').children()[7].textContent);
      // ClassicEditor.instances['mytextarea'].setData($(current).closest('tr').children()[7].textContent);
      console.log($(current).closest('tr').children()[7].textContent);
      $("#imgurl").val($(current).closest('tr').children()[8].textContent);
      $("#avoidingterms").val($(current).closest('tr').children()[9].textContent);
      $("#infosource").val($(current).closest('tr').children()[10].textContent);
    }

    function showorderdetails(current){
      console.log("showorderdetails called");
      // $("#oid").text($(current).closest('tr').children()[1].textContent);
      $("#url").text($(current).closest('tr').children()[0].textContent);
      $("#odate").text($(current).closest('tr').children()[6].textContent);
      YourEditor.setData($(current).closest('tr').children()[3].textContent);
      // $("#odetails").text($(current).closest('tr').children()[5].textContent);
      $("#chklnk").text($(current).closest('tr').children()[0].textContent);;
      $("#chklnk").prop("href", "https://"+$(current).closest('tr').children()[0].textContent)
      htmlstring = $(current).closest('tr').children()[5].textContent;
      var imgSrc = $(htmlstring).find('img').attr('src');
      $("#imgurl").attr("src", imgSrc);
      $("#title").text($(current).closest('tr').children()[2].textContent);
      $("#pubon").text($(current).closest('tr').children()[0].textContent);
      var compdate = $(current).closest('tr').children()[8].textContent.trim();
      var spanElem = $("#compdate");
      if (compdate !== 'None') {
        spanElem.text(compdate).addClass('badge badge-success');
      } else {
        spanElem.text(compdate).addClass('badge badge-warning');
        spanElem.text(compdate).text('Order in process');
      }
      $("#oprice").text("$ "+ $(current).closest('tr').children()[11].textContent);
      $("#pmethod").text($(current).closest('tr').children()[13].textContent);
      $("#pstatus").text($(current).closest('tr').children()[14].textContent);
      // $("#compdate").text($(current).closest('tr').children()[10  ].textContent);
    }  
  
      // $('#dbutton').click(function(){
      //   alert('hey');
      // $("#myModal").modal("show");
      // $("#title").val($(this).closest('tr').children()[0].textContent);
      // $("#mdlname").val($(this).closest('tr').children()[1].textContent);
      // $("#txtlname").val($(this).closest('tr').children()[2].textContent);
      // });


  
  // const downloadButton = document.getElementById('#download-button');
  // downloadButton.addEventListener('click', function() {
  //   alert('hello');
  // });








