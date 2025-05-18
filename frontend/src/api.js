export async function fetchMessage() {
  const res = await fetch('/api/message');
  const data = await res.json();
  return data.message;
}

export async function fetchLLMData() {
  const res = await fetch('/api/llm-data');
  return res.json();
}
