function handleReply(response_id) {
    const reply_form_container = document.querySelector(`#reply-form-container-${response_id}`)
    const show_form_button = document.querySelector(`#show-form-${response_id}`)

    if (reply_form_container) {
        if (reply_form_container.style.display === 'block') {
            reply_form_container.style.display = 'none';
            show_form_button.innerText = "Reply"
        }
        else {
            reply_form_container.style.display = 'block';
            show_form_button.innerText = "Cancel"
        }
    }
}
