const input_number = document.getElementById('inputNumber')

const socket = io.connect('https://pimemorizer.onrender.com');

// const socket = io.connect('http://192.168.1.20:5000');
let timerrr = false;

const score_container = document.getElementById('score-container')
const pi_value = document.querySelector('.pi-value')
const value_of_pi = "141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955321165344987202755960236480665499119881834797753566369807426542527862551818417574672890977772793800081647060016145249192173217214772350141441973568548161361157352552133475741849468438523323907394143334547762416862518983569485562099219222184272550254256887671790494601653466804988627232791786085784383827967976681454100953883786360950680064225125205117392984896084128488626945604241965285022210661186306744278622039194945047123713786960956364371917287467764657573962413890865832645995813390478027590099465764078951269468398352595709825822620522489407726719478268482601476990902640136394437455305068203496252451749399651431429809190659250937221696461515709858387410597885959772975498930161753928468138268683868942774155991855925245953959431049972524680845987273644695848653836736222626099124608051243884390451244136549762780797715691435997700129616089441694868555848406353422072225828488648158456028506016842739452267467678895252138522549954666727823986456596116354886230577456498035593634568174324112515076069479451096596094025228879710893145669136867228748940560101503308617928680920874760917824938589009714909675985261365549781893129784821682998948722658804857564014270477555132379641451523746234364542858444795265867821051141354735739523113427166102135969536231442952484937187110145765403590279934403742007310578539062198387447808478489683321445713868751943506430218453191048481005370614680674919278191197939952061419663428754440643745123718192179998391015919561814675142691239748940907186494231961567945208095146550225231603881930142093762137855956638937787083039069792077346722182562599661501421503068038447734549202605414665925201497442850732518666002132434088190710486331734649651453905796268561005508106658796998163574736384052571459102897064140110971206280439039759515677157700420337869936007230558763176359421873125147120532928191826186125867321579198414848829164470609575270695722091756711672291098169091528017350671274858322287183520935396572512108357915136988209144421006751033467110314126711136990865851639831501970165151168517143765761835155650884909989859982387345528331635507647918535893226185489632132933089857064204675259070915481416549859461637180270981994309924488957571282890592323326097299712084433573265489382391193259746366730583604142813883032038249037589852437441702913276561809377344403070746921120191302033038019762110110044929321516084244485265586003014374550256"

let score = 0
let i = 0
let time = 0

window.addEventListener("keydown", function(event){
     let value = document.getElementById('inputNumber').value
     if (event.code === "Space") { 
          event.preventDefault();
          
          if(value == value_of_pi[i]){
               i += 1
               score  += 1
               console.log('correct')
               pi_value.innerHTML += value_of_pi[i-1];
               
          }else{
               console.log('wrong')
               i = 0
               
               
               
               pi_value.innerHTML = "3."
               resetTimer()
               

         
               
          }
          document.getElementById('inputNumber').value = ""
          score_container.innerText = score
      }
})

function sendNumber(number){
     document.getElementById('inputNumber').value = number
  
}

function sendValueToCheck(){
     let value = document.getElementById('inputNumber').value
  
         
          
          if(value == value_of_pi[i]){
               i += 1
               score  += 1
               console.log('correct')
               pi_value.innerHTML += value_of_pi[i-1];
               
          }else{
               console.log('wrong')
               i = 0
               resetTimer()
               socket.emit('update-highscore', {score})
               
               pi_value.innerHTML = "3."
          }
          document.getElementById('inputNumber').value = ""
          score_container.innerText = score
     
}

function startGame(){
     document.querySelector('.start-popup').style.display = 'none'
     document.querySelector('.countdown-container').style.display = 'flex'
     
     
     startCountdown(2)
     
}

function startCountdown(duration) {
     let timer = duration;
     let countdownElement = document.getElementById("countdown");
 

     updateDisplay(timer);
 
     let countdownInterval = setInterval(function () {
         timer--; 
         updateDisplay(timer);
 
         if (timer <= 0) {
             clearInterval(countdownInterval);
             document.querySelector('.countdown-container').style.display = 'none'
             document.getElementById('try-again-popup').style.display = 'none'
             timerrr = true;

          stopWatch();
         }
     }, 1000);
 
     function updateDisplay(time) {
         let minutes = Math.floor(time / 60);
         let seconds = time % 60;
         countdownElement.textContent = seconds;
     }
 }

let hour = 0;
let minute = 0;
let second = 0;
let count = 0;
 function stopWatch() {
     
     if (timerrr) {
         
         count++;
 
         if (count == 100) {
             second++;
             count = 0;
         }
 
         if (second == 60) {
             minute++;
             second = 0;
         }
 
         if (minute == 60) {
             hour++;
             minute = 0;
             second = 0;
         }
 
         let hrString = hour;
         let minString = minute;
         let secString = second;
         let countString = count;
 
         if (hour < 10) {
             hrString = "0" + hrString;
         }
 
         if (minute < 10) {
             minString = "0" + minString;
         }
 
         if (second < 10) {
             secString = "0" + secString;
         }
 
         if (count < 10) {
             countString = "0" + countString;
         }
 
         document.getElementById('hr').innerHTML = hrString;
         document.getElementById('min').innerHTML = minString;
         document.getElementById('sec').innerHTML = secString;
         document.getElementById('count').innerHTML = countString;
         
         setTimeout(stopWatch, 10);
     }

     
     
 }
 
function resetTimer() {
     
     
     time = second
     let avgScore = score/time

     socket.emit('update-speed', {avgScore})
     socket.emit('update-highscore', {score})

     document.getElementById('try-again-popup').style.display = 'flex'
     document.getElementById('game-speed').innerHTML = "Speed: ";
     document.getElementById('game-score').innerHTML = "Score: ";
     document.getElementById('game-speed').innerHTML += `<span>${avgScore.toFixed(2)}</span>`;
     document.getElementById('game-score').innerHTML += `<span>${score}</span>`;

     
     
     score = 0
     timerrr = false;
     hour = 0;
     minute = 0;
     second = 0;
     count = 0;
     document.getElementById('hr').innerHTML = "00";
     document.getElementById('min').innerHTML = "00";
     document.getElementById('sec').innerHTML = "00";
     document.getElementById('count').innerHTML = "00";

    
 };

 function logout(){
     window.location.href = '/logout'
 }
 
 






