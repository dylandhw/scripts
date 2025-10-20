const test = //"webhook url";
  async function sendMessage() {
    const payload = { content: "some annoying message" };
    await fetch(test, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
  };

setInterval(sendMessage, 5);
