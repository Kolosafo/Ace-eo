//Make a function that checks the textContent passed into the optimization description input
//Strike off an instruction based on the input textContent passed in
//Set a score that increases based on the the amount of strike off's in the instructions
//If all instructions are cleared, Let optimization score be 100%

    console.log("Hi")
    console.log("Working up")

 
//  THIS FUNCTION WORKS ONINPUT!!!!
function strikeoff(){


      //get the textContent of the title input area
    title_textContent =  document.getElementById("id_title").value.toLowerCase()
    //get the textContent of the description input area
    var desc_textContent = document.getElementById("id_description").value.toLowerCase();
    
    //here find the length/number of words in the title field and set to a variable
    var title_split = title_textContent.split(" ")
    var title_length = title_split.length;
    

    //initiate the Splitted title textContents into a list to later compare it with that of the description
    title_words= []
    title_words.push(title_split)
    //console.log(title_words)


    //SET DESCRIPTION textContentS TO AN ARRAY LIMITED TO THE INDEX AT THE NUMBER OF WORDS IN THE TITLE
    //BETTER UNDERSTANDING --> SPLIT DESCRIPTION textContentS AND STOP AT 'TITLE LENGTH' INDEX NUMBER
    var words = desc_textContent.split(" ", title_length)
    each_desc_textContent = desc_textContent.split(" ")
    var desc_words = []
    desc_words.push(words)

    desc_length = desc_textContent.split(" ").length;
    
    //compare the two arrays and strike off if they are both equal
    if (JSON.stringify(desc_words) === JSON.stringify(title_words)){
      document.getElementById("first-point").style = "text-decoration: line-through";
    } 

    if(JSON.stringify(desc_words) !== JSON.stringify(title_words)){
      document.getElementById("first-point").style = "text-decoration: None";
      
    }
   

    
      
    
    //NEW STRATEGY



    //HERE WE MAKE THE PROGRAM STRIKE OFF 'Write upt to 50 Words'
    console.log("Cache checker")
    if (desc_length >= 50){
      document.getElementById("50-words").style = "text-decoration: line-through";
    }
    else{document.getElementById("50-words").style = "text-decoration: None";}

    if (desc_length >= 20){
      document.getElementById("20-words").style = "text-decoration: line-through";
    }
    else{document.getElementById("20-words").style = "text-decoration: None";}
    


//HERE WE MAKE THE PROGRAM STRIKE OFF 'partial matches'
const algo = (arr) => {
  const sorted = [...arr].sort();
  let matches = [];
  for (let i = 0; i < sorted.length; ) {
      const last_appearence = sorted.lastIndexOf(sorted[i]);
      if (last_appearence - i >= 4) {
          matches.push(sorted[i]);
          
      }
      
      i = last_appearence + 1;
    
     
  }

for (let j=0; j<title_length; j++){
   if (matches.includes(title_split[j])){
      document.getElementById("partial-matches").style = "text-decoration: line-through";
      console.log("Yes!")
    }
}
return matches
};

const P_match = algo(each_desc_textContent)

 




//THIS FUNCTION SHOULD INCREMENT THE METER GUAGE IF ANY SEO REQUIREMENT ABOVE IS SATISFIED!

     
    //THE METER GAUGE JS
const gaugeElement = document.querySelector(".Seo_gauge");

function setGaugetextContent(gauge, textContent) {
  
  if (textContent < 0 || textContent > 1) {
    return;
  }

  gauge.querySelector(".gauge__fill").style.transform = `rotate(${
    textContent / 2
  }turn)`;
  gauge.querySelector(".gauge__cover").textContent = `${Math.round(
    textContent * 100
  )}%`;
}


const checkStrike1 = document.getElementById("first-point").style.textDecoration
const checkStrike2 = document.getElementById("50-words").style.textDecoration
const checkStrike3 = document.getElementById("partial-matches").style.textDecoration


gauge_display = document.querySelector(".gauge__fill").style="visibility: None;"

let textContentDefault = 0

if (checkStrike1 == "line-through"){
textContentDefault += 0.33;
console.log(textContentDefault)
}else{textContentDefault = textContentDefault}

if (checkStrike2 == "line-through"){
  textContentDefault += 0.34;
  console.log(textContentDefault)
  }else{textContentDefault = textContentDefault}


if (checkStrike3 == "line-through"){
textContentDefault += 0.33;
console.log(textContentDefault)
}else{textContentDefault = textContentDefault}

for (let i=0; i<100; i++){
  
     if (textContentDefault<=0.33){
        i+=33.33
        document.querySelector(".gauge__fill").style = "background: #2ea91d"     
     }

     else if (textContentDefault<=0.66){
         i+=33.33
         document.querySelector(".gauge__fill").style = "background: #ff9805"
     }
     else if (textContentDefault<=1){
         i+=33.33
         document.querySelector(".gauge__fill").style = "background: #ed2117"
     }
 }

setGaugetextContent(gaugeElement, textContentDefault);


//This is the end of the "Oninput" function
}

    
//A function that allows users to optimize their keywords in same page






      //tHIS FUNCTION GETS KEYWORD ENTERED BY USER
 

      function theKeyword(){
        var keyword = document.getElementById("keyword_getter").textContent; 
      }
  



//THIS FUNCTION GETS TAGS AND COPY THEM BASED ON BUTTON CLICKED
var tag1 = document.getElementById("tag-2")

// Get the ID of the button that was clicked
function getID(btn){
  globalThis.tag_Btn_Id = btn.id;
  //alert(btn.id)
      }


//Initializing Getting the individual tag according to the button clicked
function copyTags(){


//Finding out what button was clicked

switch(tag_Btn_Id){
  case "copy-tag-1":
    globalThis.tag = document.getElementById("tag-1").textContent
    document.getElementById("copy-tag-1").textContent = "Copied"
    

     
    break;
  
  case "copy-tag-2":
    globalThis.tag = document.getElementById("tag-2").textContent
    document.getElementById("copy-tag-2").textContent = "Copied"
    

     
      break;
  case "copy-tag-3":
    globalThis.tag = document.getElementById("tag-3").textContent
    document.getElementById("copy-tag-3").textContent = "Copied"
    

     
      break;
  case "copy-tag-4":
  globalThis.tag = document.getElementById("tag-4").textContent
  document.getElementById("copy-tag-4").textContent = "Copied"
  

     
      break;
  case "copy-tag-5":
    globalThis.tag = document.getElementById("tag-5").textContent
    document.getElementById("copy-tag-5").textContent = "Copied"
    

     
      break;
  case "copy-tag-6":
    globalThis.tag = document.getElementById("tag-6").textContent
    document.getElementById("copy-tag-6").textContent = "Copied"
    

     
      break;
  case "copy-tag-7":
    globalThis.tag = document.getElementById("tag-7").textContent
    document.getElementById("copy-tag-7").textContent = "Copied"
    

     
      break;
  case "copy-tag-8":
    globalThis.tag = document.getElementById("tag-8").textContent
    document.getElementById("copy-tag-8").textContent = "Copied"
    

     
      break;
  case "copy-tag-9":
    globalThis.tag = document.getElementById("tag-9").textContent
    document.getElementById("copy-tag-9").textContent = "Copied"
    

     
      break;
  case "copy-tag-10":
    globalThis.tag = document.getElementById("tag-10").textContent
    document.getElementById("copy-tag-1").textContent = "Copied"
    

     
      break;
  default:
    globalThis.tag = document.getElementById("tag-1").textContent
}



//Copy the tag the coreesponds to the right button clicked

let ourText = tag.replace(/[\[\]']+/g,'');
console.log(ourText)
let textarea = document.createElement('textarea');
textarea.width = '1px';
textarea.height = '1px';
textarea.textContent = ourText;
document.body.append(textarea);
textarea.select();
document.execCommand('copy');
textarea.style = "display: None"

}

function getMeta(){

  //Getting the inputted data and appending to textarea carrying the data to view page
let get_title_textContent =  document.getElementById("id_title").value;
let get_desc_textContent =  document.getElementById("id_description").value;
let get_tags_textContent =  document.getElementById("id_tags").value;


let opt_title = document.getElementById("opt_title")
let opt_description = document.getElementById("opt_description")
let opt_tags = document.getElementById("opt_tags")
opt_title.textContent = get_title_textContent;
opt_description.textContent = get_desc_textContent;
opt_tags.textContent = get_tags_textContent;

}




  




  
  
  

      

  




