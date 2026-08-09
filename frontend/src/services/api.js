const API_URL =
  import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function healthCheck() {
  const response = await fetch(`${API_URL}/health`);

  if (!response.ok) {
    throw new Error("Loved AI API is unavailable");
  }

  return response.json();
}

export async function createProfile(profile) {
  const response = await fetch(`${API_URL}/api/profiles`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(profile),
  });

  if (!response.ok) {
    throw new Error("Unable to create profile");
  }

  return response.json();
}

export async function createMatch(userId, targetUserId) {
  const response = await fetch(`${API_URL}/api/matches`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      user_id: userId,
      target_user_id: targetUserId
    }),
  });

  if (!response.ok) {
    throw new Error("Unable to create match");
  }

  return response.json();
}
