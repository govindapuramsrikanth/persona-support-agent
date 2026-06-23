// Load old messages when page opens
window.onload = function () {

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





function saveChat(type, message) {


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






async function sendMessage() {


    let input = document.getElementById("user-input")


    let question = input.value



    if (question.trim() === "") {
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





    try {


        let response = await fetch(
            "https://persona-support-agent-q4pf.onrender.com/chat",
            {

                method: "POST",


                headers: {

                    "Content-Type": "application/json"

                },



                body: JSON.stringify(
                    {

                        message: question

                    }
                )

            }
        )




        let data = await response.json()





        // remove typing message

        document.getElementById(typingId).remove()





        // show AI answer

        chatBox.innerHTML +=
            `
            <div class="bot">
                ${data.answer}
            </div>
            `



        saveChat("bot", data.answer)




        chatBox.scrollTop = chatBox.scrollHeight


    }


    catch (error) {


        document.getElementById(typingId).remove()


        chatBox.innerHTML +=
            `
            <div class="bot">
                ❌ Server error. Please try again.
            </div>
            `


        console.log(error)

    }



}






function clearChat() {


    localStorage.removeItem("chatHistory")


    document.getElementById("chat-box").innerHTML = ""


}






document
    .getElementById("user-input")
    .addEventListener(
        "keydown",

        function (event) {


            if (event.key === "Enter") {


                sendMessage()


            }


        }

    )