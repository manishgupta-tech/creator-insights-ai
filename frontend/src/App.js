import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [videoA, setVideoA] = useState("");
  const [videoB, setVideoB] = useState("");

  const [result, setResult] = useState(null);

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const analyzeVideos = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/analyze",
        {
          video_a_url: videoA,
          video_b_url: videoB,
        }
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);
      alert("Error connecting to backend");

    }
  };

  const askQuestion = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/compare",
        {
          question: question
        }
      );

      setAnswer(
        response.data.answer
      );

    } catch (error) {

      console.error(error);
      alert("Error getting AI response");

    }
  };

  return (
    <div className="container">

      <h1>Creator Insights AI</h1>

      <input
        type="text"
        placeholder="Video A URL"
        value={videoA}
        onChange={(e) => setVideoA(e.target.value)}
      />

      <input
        type="text"
        placeholder="Video B URL"
        value={videoB}
        onChange={(e) => setVideoB(e.target.value)}
      />

      <button onClick={analyzeVideos}>
        Analyze Videos
      </button>

      {result && (
        <div className="cards">

          <div className="card">
            <h2>Video A</h2>

            <p>
              <strong>Title:</strong>{" "}
              {result.video_a.metadata.title}
            </p>

            <p>
              <strong>Creator:</strong>{" "}
              {result.video_a.metadata.creator}
            </p>

            <p>
              <strong>Views:</strong>{" "}
              {result.video_a.metadata.views}
            </p>

            <p>
              <strong>Engagement:</strong>{" "}
              {result.video_a.metadata.engagement_rate}%
            </p>
          </div>

          <div className="card">
            <h2>Video B</h2>

            <p>
              <strong>Title:</strong>{" "}
              {result.video_b.metadata.title}
            </p>

            <p>
              <strong>Creator:</strong>{" "}
              {result.video_b.metadata.creator}
            </p>

            <p>
              <strong>Views:</strong>{" "}
              {result.video_b.metadata.views}
            </p>

            <p>
              <strong>Engagement:</strong>{" "}
              {result.video_b.metadata.engagement_rate}%
            </p>
          </div>

        </div>
      )}

      <div className="chat-box">

        <h2>Creator Chat</h2>

        <input
          type="text"
          placeholder="Ask a question..."
          value={question}
          onChange={(e) =>
            setQuestion(e.target.value)
          }
        />

        <button
          onClick={askQuestion}
        >
          Ask AI
        </button>

        {answer && (

          <div className="answer-box">

            <h3>Answer</h3>

            <p>{answer}</p>

          </div>

        )}

      </div>

    </div>
  );
}

export default App;