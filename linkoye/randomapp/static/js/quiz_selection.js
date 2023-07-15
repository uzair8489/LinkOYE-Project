var yes = document.querySelectorAll('.yes');
var no = document.querySelectorAll('.no');
var response = document.querySelectorAll('#response');
var quizShow = document.querySelectorAll('.quiz_show');
const val = document.querySelectorAll('.input_text');
const submitbtn = document.querySelector('#click');
const result_percentage = document.querySelector('#result_percentage');
var i = 1;  
document.querySelector('#result').style.display='none';
document.querySelector('#submit_btn').style.display = 'none'
var no_of_no = 0;
var no_of_yes = 0;
var count;
var result;
for(var n= 1 ; n < quizShow.length ; n++){
    quizShow[n].style.display = 'none'
    yes[n - 1].addEventListener('click' ,function(){
        
        yes[i-1].disabled = true;
        no[i-1].disabled = true;
        no[i-1].style.background = '#00aacc';
        yes[i-1].style.background = '#00aacc';
        quizShow[i].style.display = 'block'
        quizShow[i-1].style.opacity = '0.5'
        response[i-1].innerHTML = 'You have selected this : YES'
        document.querySelectorAll('.input_text')[i-1].value = 'YES'
        no_of_yes += 1;
        count = no_of_yes;
        yes[quizShow.length-1].addEventListener('click' ,function(){
            no[i-1].style.background = '#00aacc';
            yes[i-1].style.background = '#00aacc';
            yes[quizShow.length-1].disabled = true;
            no[quizShow.length-1].disabled = true;
            quizShow[quizShow.length-1].style.opacity = '0.5'
            response[quizShow.length-1].innerHTML = 'You have selected this : YES'
            document.querySelectorAll('.input_text')[quizShow.length-1].value = 'YES'
            document.querySelector('#submit_btn').style.display = 'block'
            count = no_of_yes + 1;
            result = ((count / quizShow.length ) * 100)
            result_percentage.value = 'You Have '+result.toFixed(2) +'%  chances of Melanoma Cancer.'
        })
        i++;
    })
    no[n - 1].addEventListener('click' ,function(){
        
        no[i-1].disabled = true;
        no[i-1].style.background = '#00aacc';
        yes[i-1].style.background = '#00aacc';
        yes[i-1].disabled = true;
        quizShow[i].style.display = 'block'
        quizShow[i-1].style.opacity = '0.5'
        response[i-1].innerHTML = 'You have selected this : NO'
        document.querySelectorAll('.input_text')[i-1].value = 'NO'
        no_of_no += 1;
        count = no_of_no;
        no[quizShow.length-1].addEventListener('click' ,function(){
            no[i-1].style.background = '#00aacc';
            yes[i-1].style.background = '#00aacc';
            yes[quizShow.length-1].disabled = true;
            no[quizShow.length-1].disabled = true;
            quizShow[quizShow.length-1].style.opacity = '0.5'
            response[quizShow.length-1].innerHTML = 'You have selected this : NO'
            document.querySelectorAll('.input_text')[quizShow.length-1].value = 'NO'
            document.querySelector('#submit_btn').style.display = 'block';
            count = no_of_no + 1;
            result = ((count / quizShow.length ) * 100)
            result_percentage.value = 'You have '+result.toFixed(2) +'% chances of not having Melanoma Cancer.'
        })
        i++;
    })
    
    

}


