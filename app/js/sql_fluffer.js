const Editor = ({ placeHolder, onChange, value, readOnly }) => {
  return (
    <textarea
      className="editor"
      placeholder={placeHolder}
      onChange={onChange}
      value={value}
      readOnly={readOnly}
    ></textarea>
  );
};

const App = () => {
  const [sql, setSql] = React.useState("");
  const [fixedSql, setFixedSql] = React.useState("");
  const [lint, setLint] = React.useState("");

  const fluffSql = () => {
    const endpoint = "https://sql-fluffer.herokuapp.com/fluff/";
    // const endpoint = "http://localhost:8000/fluff/";
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sql: sql }),
    };
    fetch(endpoint, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setFixedSql(data["fixed"]);
        setLint(data["lint"]);
      });
  };

  return (
    <div className="app">
      <div className="container">
        <Editor
          placeHolder="Type your code here..."
          onChange={(e) => setSql(e.target.value)}
          readOnly={false}
        />
        <Editor
          class="fixed"
          placeHolder="Fixed SQL goes here"
          value={fixedSql}
          readOnly={true}
        />
      </div>
      <hr />
      <button onClick={fluffSql}>fluff it!</button>
      {lint ? (
        <ul>
          {lint.map((l) => (
            <li>
              {l.code} - {l.description}
            </li>
          ))}
        </ul>
      ) : (
        <h3>no lint!</h3>
      )}
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById("sql_container"));
