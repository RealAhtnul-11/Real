from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

SLIDESHOWS = [
    {
        "user": "@luna_gray",
        "caption": "Night streets in monochrome.",
        "images": ["City lights", "Crosswalk", "Neon reflections"],
        "likes": 1284,
        "comments": 42,
        "verified": True,
    },
    {
        "user": "@noir_frames",
        "caption": "Studio portraits, soft shadows.",
        "images": ["Pose one", "Pose two", "Pose three", "Pose four"],
        "likes": 987,
        "comments": 18,
        "verified": False,
    },
    {
        "user": "@grayscale.daily",
        "caption": "Café textures and quiet moments.",
        "images": ["Cup", "Notebook", "Window"],
        "likes": 432,
        "comments": 9,
        "verified": True,
    },
]


@app.route("/")
def index():
    return render_template("index.html", slideshows=SLIDESHOWS)


@app.route("/explore")
def explore():
    return render_template(
        "page.html",
        title="Explore",
        subtitle="Discover monochrome creators and trending slides.",
    )


@app.route("/slides")
def slides():
    return render_template(
        "page.html",
        title="Slides",
        subtitle="Short-form highlights and featured slide collections.",
    )


@app.route("/messages")
def messages():
    conversations = [
        {
            "user": "@luna_gray",
            "status": "Active now",
            "snippet": "Just posted a new monochrome set.",
            "unread": 2,
            "verified": True,
        },
        {
            "user": "@noir_frames",
            "status": "Seen 2h ago",
            "snippet": "Want to collaborate on a studio shoot?",
            "unread": 0,
            "verified": False,
        },
        {
            "user": "@grayscale.daily",
            "status": "Typing…",
            "snippet": "The café series is live!",
            "unread": 1,
            "verified": True,
        },
    ]
    messages_feed = [
        {
            "sender": "@luna_gray",
            "time": "2m",
            "text": "Uploading a new slideshow now.",
            "inbound": True,
        },
        {
            "sender": "You",
            "time": "1m",
            "text": "Can’t wait to see it. Sharing mine too.",
            "inbound": False,
        },
        {
            "sender": "@luna_gray",
            "time": "Just now",
            "text": "Sent you the preview frames.",
            "inbound": True,
        },
    ]
    return render_template(
        "messages.html",
        conversations=conversations,
        messages_feed=messages_feed,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("index"))
    return render_template(
        "auth.html",
        title="Log in to Slides",
        subtitle="Use your email and a one-time code or password to sign in.",
        submit_label="Log in",
        swap_label="Need an account? Sign up",
        swap_url=url_for("signup"),
        form_type="login",
    )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        return redirect(url_for("index"))
    return render_template(
        "auth.html",
        title="Create your Slides account",
        subtitle="Set up your profile with email, username, and a secure password.",
        submit_label="Create account",
        swap_label="Already have an account? Log in",
        swap_url=url_for("login"),
        form_type="signup",
    )


@app.route("/logout")
def logout():
    return redirect(url_for("login"))


@app.route("/profile")
def profile():
    return render_template(
        "page.html",
        title="Profile",
        subtitle="Manage your bio, posts, and slideshow archives.",
    )


@app.route("/profile/<username>")
def profile_detail(username):
    return render_template(
        "page.html",
        title=f"Profile: @{username}",
        subtitle="Follow the creator and browse their latest slideshows.",
    )


@app.route("/create/post")
def create_post():
    return render_template(
        "page.html",
        title="Create Post",
        subtitle="Draft a new monochrome post and share it with your followers.",
    )


@app.route("/create/slide")
def create_slide():
    return render_template(
        "page.html",
        title="Create Slide",
        subtitle="Add a single highlight slide with a short caption.",
    )


@app.route("/create/slideshow")
def create_slideshow():
    return render_template(
        "page.html",
        title="Create Slideshow",
        subtitle="Upload and arrange a multi-frame monochrome slideshow.",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
