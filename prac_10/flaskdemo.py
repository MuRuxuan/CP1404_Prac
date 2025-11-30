from flask import Flask, render_template, request, redirect, url_for, session
import wikipedia
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'IT@JCUA0Zr98j/3yXa R~XHH!jmN]LWX/,?RT'

# Configure Wikipedia
wikipedia.set_lang("en")
wikipedia.set_rate_limiting(True)


@app.route('/')
def home():
    """Home page route."""
    return render_template("home.html")


@app.route('/about')
def about():
    """About page route."""
    fun_facts = [
        "Wikipedia has over 55 million articles in 300+ languages",
        "The English Wikipedia is the largest with over 6 million articles",
        "Wikipedia is maintained by volunteers worldwide",
        "Jimmy Wales and Larry Sanger founded Wikipedia in 2001"
    ]
    return render_template("about.html", fun_facts=fun_facts)


@app.route('/search', methods=['POST', 'GET'])
def search():
    """Search page route."""
    if request.method == 'POST':
        session['search_term'] = request.form['search']
        return redirect(url_for('results'))
    return render_template("search.html")


@app.route('/results')
def results():
    """Results page route."""
    search_term = session.get('search_term', 'Python')

    try:
        page = get_page(search_term)
        # Get page summary for additional info
        summary = wikipedia.summary(search_term, sentences=2)
    except Exception as e:
        page = None
        summary = f"Error: {str(e)}"

    # Get random fact for fun
    random_fact = get_random_fact()

    return render_template("results.html",
                           page=page,
                           summary=summary,
                           search_term=search_term,
                           random_fact=random_fact)


@app.route('/random')
def random_page():
    """Get a random Wikipedia page."""
    try:
        random_title = wikipedia.random()
        session['search_term'] = random_title
        return redirect(url_for('results'))
    except:
        return redirect(url_for('home'))


@app.route('/history')
def history():
    """Show search history."""
    search_history = session.get('search_history', [])
    return render_template("history.html", search_history=search_history)


def get_page(search_term):
    """Get a Wikipedia page object based on the search term."""
    try:
        page = wikipedia.page(search_term)
        # Add to search history
        add_to_history(search_term, page.title)
        return page
    except wikipedia.exceptions.PageError:
        # No such page, get a random one
        random_title = wikipedia.random()
        return wikipedia.page(random_title)
    except wikipedia.exceptions.DisambiguationError as e:
        # Get the first option from disambiguation
        return wikipedia.page(e.options[0])


def add_to_history(search_term, page_title):
    """Add search to session history."""
    if 'search_history' not in session:
        session['search_history'] = []

    history_entry = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'searched': search_term,
        'found': page_title
    }

    session['search_history'].append(history_entry)
    # Keep only last 10 searches
    session['search_history'] = session['search_history'][-10:]
    session.modified = True


def get_random_fact():
    """Return a random fun fact."""
    facts = [
        "Did you know? Wikipedia has no ads and is funded by donations.",
        "Fun fact: Over 200,000 volunteers edit Wikipedia regularly.",
        "Interesting: Wikipedia is one of the top 10 most visited websites.",
        "Trivia: The Wikipedia logo is an unfinished globe made of puzzle pieces.",
        "Cool fact: Anyone can edit Wikipedia (but changes are reviewed)."
    ]
    return random.choice(facts)


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/results')
def results():
    """Results page route. Render the search results."""
    search_term = session['search_term']
    page = get_page(search_term)
    return render_template("results.html", page=page)


def get_page(search_term):
    """Get a Wikipedia page object based on the search term."""
    # This function is not a route
    try:
        page = wikipedia.page(search_term)
    except wikipedia.exceptions.PageError:
        # No such page, so return a random one
        page = wikipedia.page(wikipedia.random())
    except wikipedia.exceptions.DisambiguationError:
        # This is a disambiguation page; get the first real page (close enough)
        page_titles = wikipedia.search(search_term)
        # Sometimes the next page has the same name (different caps), so don't try the same again
        if page_titles[1].lower() == page_titles[0].lower():
            title = page_titles[2]
        else:
            title = page_titles[1]
        page = get_page(wikipedia.page(title))
    return page


if __name__ == '__main__':
    app.run()
