import "./App.css";

function App() {
  return (
    <div className="loved-app">
      <header className="loved-header">
        <div className="logo">♥ Loved AI</div>

        <button className="header-button">
          ☰
        </button>
      </header>

      <main className="discovery">

        <section className="stories">
          <button className="story add-story">
            <span>+</span>
            <small>Your Story</small>
          </button>

          {["Maya", "Jordan", "Sofia", "Alex"].map(
            (name) => (
              <button
                className="story"
                key={name}
              >
                <div className="story-ring">
                  <div className="story-avatar">
                    {name[0]}
                  </div>
                </div>

                <small>{name}</small>
              </button>
            )
          )}
        </section>

        <section className="profile-card">

          <div className="profile-media">
            <div className="video-placeholder">
              <span>▶</span>
            </div>

            <div className="profile-gradient" />

            <div className="profile-info">

              <div className="compatibility">
                92% Compatible
              </div>

              <h1>Maya, 27</h1>

              <p>Houston, TX</p>

              <div className="interests">
                <span>Music</span>
                <span>Travel</span>
                <span>Food</span>
              </div>

            </div>
          </div>

          <div className="profile-actions">
            <button className="pass">✕</button>
            <button className="like">♥</button>
            <button className="chat">💬</button>
            <button className="video">📹</button>
          </div>

        </section>

      </main>

      <nav className="bottom-nav">
        <button>⌂<small>Discover</small></button>
        <button>♥<small>Matches</small></button>
        <button>💬<small>Chats</small></button>
        <button>👤<small>Profile</small></button>
      </nav>

    </div>
  );
}

export default App;
