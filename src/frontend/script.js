// Load old messages when page opens
window.onload = function(){

    let oldChats = JSON.parse(localStorage.getItem("chatHistory")) || []

    let chatBox = document.getElementById("chat-box")


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





function saveChat(type, message){


    let chats = JSON.parse(localStorage.getItem("chatHistory")) || []


    chats.push(
        {
            type: type,
            message: message
        }
    )


    localStorage.setItem(
        "chatHistory",
        JSON.stringify(chats)
    )

}





async function sendMessage(){


    let input = document.getElementById("user-input")


    let question = input.value



    if(question.trim() === ""){
        return
    }



    let chatBox = document.getElementById("chat-box")




    // show user message

    chatBox.innerHTML +=
    `
    <div class="user">
        ${question}
    </div>
    `


    saveChat("user", question)



    input.value = ""




    // typing animation

    let typingId = "typing"


    chatBox.innerHTML +=
    `
    <div class="bot" id="${typingId}">
        🤖 AI is typing...
    </div>
    `


    chatBox.scrollTop = chatBox.scrollHeight





    let response = await fetch(
        "http://127.0.0.1:8000/chat",
        {

            method: "POST",


            headers: {

                "Content-Type": "application/json"

            },


            body: JSON.stringify(
                {
                    question: question
                }
            )

        }
    )




    let data = await response.json()




    // remove typing

    document.getElementById(typingId).remove()




    // show bot message

    chatBox.innerHTML +=
    `
    <div class="bot">
        ${data.answer}
    </div>
    `



    saveChat("bot", data.answer)




    chatBox.scrollTop = chatBox.scrollHeight


}



function clearChat(){


    localStorage.removeItem("chatHistory")


    document.getElementById("chat-box").innerHTML = ""


}




document
.getElementById("user-input")
.addEventListener(
    "keydown",
    function(event){


        if(event.key === "Enter"){


            sendMessage()


        }


    }
)