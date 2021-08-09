//Make a function that checks the value passed into the optimization description input
//Strike off an instruction based on the input value passed in
//Set a score that increases based on the the amount of strike off's in the instructions
//If all instructions are cleared, Let optimization score be 100%

    console.log("Hi")
 
  

//  THIS FUNCTION WORKS ONINPUT!!!!
function strikeoff(){


      //get the value of the title input area
    title_value =  document.getElementById("id_title").value.toLowerCase()
    //get the value of the description input area
    var desc_value = document.getElementById("id_description").value.toLowerCase();
    
    //here find the length/number of words in the title field and set to a variable
    var title_split = title_value.split(" ")
    var title_length = title_split.length;
    

    //initiate the Splitted title values into a list to later compare it with that of the description
    title_words= []
    title_words.push(title_split)
    //console.log(title_words)


    //SET DESCRIPTION VALUES TO AN ARRAY LIMITED TO THE INDEX AT THE NUMBER OF WORDS IN THE TITLE
    //BETTER UNDERSTANDING --> SPLIT DESCRIPTION VALUES AND STOP AT 'TITLE LENGTH' INDEX NUMBER
    var words = desc_value.split(" ", title_length)
    each_desc_value = desc_value.split(" ")
    var desc_words = []
    desc_words.push(words)

    desc_length = desc_value.split(" ").length;
    
    //compare the two arrays and strike off if they are both equal
    if (JSON.stringify(desc_words) === JSON.stringify(title_words)){
      document.getElementById("first-point").style = "text-decoration: line-through";
    } 

    if(JSON.stringify(desc_words) !== JSON.stringify(title_words)){
      document.getElementById("first-point").style = "text-decoration: None";
      
    }
   

    
      
    
    //NEW STRATEGY



    //HERE WE MAKE THE PROGRAM STRIKE OFF 'Write upt to 50 Words'
    if (desc_length >= 50){
      document.getElementById("50-words").style = "text-decoration: line-through";
    }
    else{document.getElementById("50-words").style = "text-decoration: None";}
    


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

const P_match = algo(each_desc_value)
console.log(P_match)
console.log(title_split)
 




//THIS FUNCTION SHOULD INCREMENT THE METER GUAGE IF ANY SEO REQUIREMENT ABOVE IS SATISFIED!

     
    //THE METER GAUGE JS
const gaugeElement = document.querySelector(".gauge");

function setGaugeValue(gauge, value) {
  
  if (value < 0 || value > 1) {
    return;
  }

  gauge.querySelector(".gauge__fill").style.transform = `rotate(${
    value / 2
  }turn)`;
  gauge.querySelector(".gauge__cover").textContent = `${Math.round(
    value * 100
  )}%`;
}



const checkStrike1 = document.getElementById("first-point").style.textDecoration
const checkStrike2 = document.getElementById("50-words").style.textDecoration
const checkStrike3 = document.getElementById("partial-matches").style.textDecoration

let valueDefault = 0

if (checkStrike1 == "line-through"){
valueDefault += 0.33;
console.log(valueDefault)
}else{valueDefault = valueDefault}

if (checkStrike2 == "line-through"){
  valueDefault += 0.34;
  console.log(valueDefault)
  }else{valueDefault = valueDefault}


if (checkStrike3 == "line-through"){
valueDefault += 0.33;
console.log(valueDefault)
}else{valueDefault = valueDefault}



setGaugeValue(gaugeElement, valueDefault);



//This is the end of the "Oninput" function
}






    
//A function that allows users to optimize their keywords in same page

function add_to_optimization(){
  //When the function is called here
  //The in-line optimization functionality/form becomes visible
 
  
  //When the user presses 'Optimize', get the value of the keyword they want to 
  //optimize from the keyword research tool and pass it in the 
  //Optimization's (Title, Description and Tags)
  var keyword = document.getElementById("keyword_form").value
  if(keyword != ''){
    document.getElementById("seo-container").style="visibility: visible;"

    //Make Meter Gauge Visible
    document.getElementById("gauge-container").style="visibility: visible;"
  }
  else if(keyword == ''){
    alert("PLEASE TYPE A VALID KEYWORD")
  }
  if (keyword){
    var description_value = document.getElementById("id_description")
    var title_value = document.getElementById("id_title")
    var tags_value = document.getElementById("id_tags")
    var user_keyword_to_thumbnails = document.getElementById('user_keyword')
    description_value.value = keyword
    user_keyword_to_thumbnails.value = keyword
    title_value.value = keyword
    tags_value.value=keyword
  }

}
// end of onClick Event

      //Testing to access animation usiung JS

  




  
  
  

      

  




