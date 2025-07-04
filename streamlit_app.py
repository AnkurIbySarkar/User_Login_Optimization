import requests
import streamlit as st

from benchmark.compare import benchmark_n_times, compare_lookup

APP_URL = "http://app:8000"  # Use `localhost` if running outside Docker

st.set_page_config(page_title="User Lookup Benchmark", layout="centered")
st.title("🔍 User Lookup Benchmark (Brute vs Cached)")

# --- Cache Control Section ---
with st.expander("Cache Controls", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Clear Redis Cache"):
            try:
                res = requests.delete(f"{APP_URL}/check/cache/flush")
                if res.status_code == 200:
                    st.success("Redis cache cleared!")
                else:
                    st.error("Failed to clear cache.")
            except Exception as e:
                st.error(f"Request failed: {e}")

    with col2:
        if st.button("Reset Cache Metrics"):
            try:
                res = requests.delete(f"{APP_URL}/metrics/cache/reset")
                if res.status_code == 200:
                    st.success("Cache metrics reset!")
                else:
                    st.error("Failed to reset metrics.")
            except Exception as e:
                st.error(f"Request failed: {e}")

# --- Metric Viewer ---
with st.expander("📊 View Cache Metrics", expanded=False):
    if st.button("🔄 Refresh Metrics"):
        try:
            metrics = requests.get(f"{APP_URL}/metrics/cache").json()
            st.metric("Cache Hits", metrics["hits"])
            st.metric("Cache Misses", metrics["misses"])
            st.bar_chart(
                {
                    "Hits": [metrics["hits"]],
                    "Misses": [metrics["misses"]],
                }
            )
        except Exception as e:
            st.error(f"Could not load cache metrics: {e}")

# --- Lookup Benchmark ---
st.header("🔍 Lookup Benchmark Test")
email = st.text_input("Enter email to test:")

batch_mode = st.toggle("🔁 Run multiple times")
runs = st.slider("How many runs?", 2, 100, 10) if batch_mode else 1

if email:
    with st.spinner("Running benchmark..."):
        if batch_mode:
            result = benchmark_n_times(email, runs)
            st.subheader("📊 Average Results")
            st.metric("Brute Avg (ms)", result["brute_avg"])
            st.metric("Cached Avg (ms)", result["cached_avg"])

            st.line_chart(
                {"Brute": result["brute_times"], "Cached": result["cached_times"]}
            )
        else:
            result = compare_lookup(email)
            st.subheader("🧪 One-time Check")
            st.metric("Brute (ms)", result["brute"]["time_ms"])
            st.metric("Cached (ms)", result["cached"]["time_ms"])

            if result["cached"]["hit"]:
                st.success("Redis Cache Hit")
            else:
                st.warning("Redis Cache Miss")
