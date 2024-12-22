let content_body = document.querySelectorAll(".theme");
let tag = document.querySelectorAll(".projcard-tag");
let date_card = document.querySelectorAll(".text-body-secondary");
let btn = document.querySelector("#checkbox"); 

content_body.forEach((content) => {
    btn.addEventListener('change',()=>{
        if(btn.checked){
            content.classList.add('dark-theme');

            console.log(content)
        }else{
            content.classList.remove('dark-theme');
        }
    })  
});

date_card.forEach((date) =>{
    if(btn.checked){
        date.classList.add("text-body-secondary")
    }
    else{
        date.classList.remove("text-body-secondary")
    }
});


// // Apply the saved theme state on page load
// const applySavedTheme = () => {
//     const isDarkMode = localStorage.getItem('dark-mode') === 'true';
//     btn.checked = isDarkMode; // Set checkbox state based on saved preference
//     content_body.forEach((content) => {
//         if (isDarkMode) {
//             content.classList.add('dark-theme');
//         } else {
//             content.classList.remove('dark-theme');
//         }
//     });
// };

// // Toggle theme and save state
// const toggleTheme = () => {
//     const isDarkMode = btn.checked;
//     localStorage.setItem('dark-mode', isDarkMode); // Save state in localStorage
//     content_body.forEach((content) => {
//         if (isDarkMode) {
//             content.classList.add('dark-theme');
//         } else {
//             content.classList.remove('dark-theme');
//         }
//     });
// };


// applySavedTheme();
// btn.addEventListener('change', toggleTheme);


// This adds some nice ellipsis to the description:
document.querySelectorAll(".projcard-description").forEach(function(box) {
    $clamp(box, {clamp: 6});
  });