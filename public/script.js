document
  .getElementById("upload-form")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById("file").files[0];
    formData.append("file", fileInput);

    try {
      const response = await fetch("/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      const resultList = document.getElementById("result-list");
      const resultsContainer = document.getElementById("results");

      // Clear previous results
      resultList.innerHTML = "";

      if (data.error) {
        resultList.innerHTML = `<li>Error: ${data.error}</li>`;
      } else {
        data.result.forEach((item, index) => {
          const li = document.createElement("li");
          li.innerHTML = `Test Case ${index + 1}: True Label = ${
            item["True label"]
          }, Predicted Label = ${item["Predicted label"]}`;
          resultList.appendChild(li);
        });
      }

      // Show results container
      resultsContainer.style.display = "block";
    } catch (error) {
      alert("An error occurred while processing the file.");
      console.error("Upload Error:", error);
    }
  });
