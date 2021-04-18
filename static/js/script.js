// let totalQuestion = questions.length;
let attempt = 0;
let score = 0;
let wrong = 0;
let index=0;
let questions = quiz.sort(function(){
    return 0.5-Math.random();
});
let totalQuestion = questions.length;
$(function(){
// timer code starts from here
let totalTime=60;
let min= 0;
let sec = 0;
let counter =0;
let timer= setInterval(function(){
counter++;
min = Math.floor((totalTime-counter)/60);
sec= totalTime -(min*60)-counter;
$(".timerBox span").text(min+":" + sec);
if( counter==totalTime){
  alert("time is over press ok to show the result");
  result();
    clearInterval(timer);
    
}
} ,1000);
// timer code ends here

//  print questions
printQuestions(index);

});

// function to print questions start here
function printQuestions(i){
// console.log(quiz);

$(".questionBox span").text(questions[i].question);
$(".optionBox span").eq(0).text(questions[i].option[0]);
$(".optionBox span").eq(1).text(questions[i].option[1]);
$(".optionBox span").eq(2).text(questions[i].option[2]);
$(".optionBox span").eq(3).text(questions[i].option[3]);

};
// function to print question end here

// functon to check answer 
function checkAnswer(option)
{
attempt++;
let optionClicked= $(option).data("opt");
if(optionClicked==questions[index].answer){
    $(option).addClass("right");
    score++;
}
else{
    $(option).addClass("wrong");
    wrong++;
}
$(".scoreBox span").text(score);
$(".optionBox span").attr("onclick","");
}
// function to check answer end here

// function for the next question start
function showNext(){
    if(index>=questions.length-1){
        showResult();
        return;
    }
    index++;
    $(".optionBox span").removeClass();
    $(".optionBox span").attr("onClick","checkAnswer(this)");
    printQuestions(index);
}
// function for the next question end

// function for result starts here
function showResult(){
    $("#questionScreen").hide();
    $("#resultScreen").show();
    $("#totalQuestions").text(totalQuestion);
    $("#attemptQuestions").text(attempt);
    $("#correctAnswers").text(score);
    $("#wrongAnswers").text(wrong);
}
// function for result ends here
// result screen automatically function
function result(){
    $("#questionScreen").hide();
    $( "#resultScreen").show();
    $("#totalQuestions").text(totalQuestion);
    $("#attemptQuestions").text(attempt);
    $("#correctAnswers").text(score);
    $("#wrongAnswers").text(wrong);
}
// result screen automatically function
