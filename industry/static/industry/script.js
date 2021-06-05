//بعد ما حكينا حكاية الفيل نحكي حكاية الدرفيل
//صللي علي النبي و عليه الصلاة و السلام
//Journey to the center of the posts function from buttom up
//1- make add post function to make dive then add class to the div then add content to the div then append a post to this class all automatically
//2-create the load function to send request to the API we made and return it's data as json then loop through it using addpost()
//3- listen when the user reach the bottom of the page using the window.scroll() with if condition to check weather the height and scroll >= initial length
//4-finally or initially load the DOMContentLoaded by an addEventListener to run the load() first time then let the  window.onscroll do the rest


console.log("static.js is loaded")

// Start with first post
let counter = 1;

// Load posts 20 at a time, or how many posts you want to load at a time
const quantity = 20;

// When DOM loads, render the first 20 posts, or call the lovely load function which will load the upcoming 20 posts as the end says
document.addEventListener('DOMContentLoaded', load);

// If scrolled to bottom, load the next 20 posts
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

// Load next set of posts
function load() {
    console.log("load functionis working")
    // Set start and end post numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    // Get new posts and add posts , from our created API, we can user others API with the same approach but read the API documentation first
    fetch(`/posts?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.posts.forEach(add_post);
    })
};

// Add a new post with given contents to DOM
function add_post(contents) {

    // Create new post, creating div then add class to the div then add content to the class then add post to the DOM which hold the posts id that we created in the HTML
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = contents;

    // Add post to DOM
    document.querySelector('#posts').append(post);
};
