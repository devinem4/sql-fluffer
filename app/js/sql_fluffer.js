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
  return (
    <div className="container">
      <Editor
        placeHolder="Type your code here..."
        onChange={(e) => setSql(e.target.value)}
        readOnly={false}
      />
      <Editor
        class="fixed"
        placeHolder="Fixed SQL goes here"
        value={sql}
        readOnly={true}
      ></Editor>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById("sql_container"));
