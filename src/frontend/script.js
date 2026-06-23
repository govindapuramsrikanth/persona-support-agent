// Load old messages when page opens
window.onload = function () {

    let oldChats = JSON.parse(localStorage.getItem("chatHistory")) || []

    let chatBox = document.getElementById("chat-box")


    if(oldChats.length === 0){

        chatBox.innerHTML =
        `
        <div class="bot">
            🤖 Hello! I am your AI Support Agent.
            <br><br>
            How can I help you today?
        </div>
        `

    }


    oldChats.forEach(chat => {

        chatBox.innerHTML +=
        `
        <div class="${chat.type}">
            ${chat.message}
        </div>
        `

    })


    chatBox.scrollTop = chatBox.scrollHeight

}



// Save chat history
function saveChat(type, message) {

    let chats = JSON.parse(localStorage.getItem("chatHistory")) || [];


    chats.push({
        type: type,
        message: message
    });


    localStorage.setItem(
        "chatHistory",
        JSON.stringify(chats)
    );

}






// Send message
async function sendMessage() {


    let input = document.getElementById("user-input");

    let question = input.value;



    if (question.trim() === "") {
        return;
    }



    let chatBox = document.getElementById("chat-box");





    // Show user message

    chatBox.innerHTML += `
        <div class="user">
            ${question}
        </div>
    `;


    saveChat("user", question);



    input.value = "";






    // Typing animation

    let typingId = "typing";


    chatBox.innerHTML += `
        <div class="bot" id="${typingId}">
            🤖 AI is typing...
        </div>
    `;


    chatBox.scrollTop = chatBox.scrollHeight;






    try {


        let response = await fetch(
            "https://persona-support-agent-g4pf.onrender.com/chat",
            {

                method: "POST",


                headers: {

                    "Content-Type": "application/json"

                },


                body: JSON.stringify({

                    message: question

                })

            }
        );




        let data = await response.json();





        // Remove typing animation

        document.getElementById(typingId).remove();






        // Format AI answer with line breaks

        let aiAnswer = data.answer.replace(/\n/g, "<br>");






        // Show AI answer

        chatBox.innerHTML += `
            <div class="bot">
                ${aiAnswer}
            </div>
        `;




        saveChat("bot", aiAnswer);



        chatBox.scrollTop = chatBox.scrollHeight;


    }


    catch (error) {


        document.getElementById(typingId).remove();



        chatBox.innerHTML += `
            <div class="bot">
                ❌ Server error. Please try again.
            </div>
        `;


        console.log(error);


    }


}







// Clear chat
function clearChat() {


    localStorage.removeItem("chatHistory");


    document.getElementById("chat-box").innerHTML = "";


}








// Send message using Enter key

document
    .getElementById("user-input")
    .addEventListener(
        "keydown",

        function (event) {


            if (event.key === "Enter") {

                sendMessage();

            }


        }

    );