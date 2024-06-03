import streamlit as st
import multiprocessing
import os

def run_crew_process(inputs, result_queue, google_api_key):
    from crewai import Crew, Process
    from agents import support_agent, support_quality_assurance_agent
    from tasks import inquiry_resolution, quality_assurance_review

    os.environ["GOOGLE_API_KEY"] = google_api_key
    #os.environ["SERPER_API_KEY"] = serper_api_key

    crew = Crew(
        agents=[support_agent, support_quality_assurance_agent],
        tasks=[inquiry_resolution, quality_assurance_review],
        process=Process.sequential,
    )

    result = crew.kickoff(inputs=inputs)
    result_queue.put(result)

if __name__ == "__main__":
    st.title("Customer Support Automation")

    # Input fields
    customer = st.text_input("Organisation name")
    person = st.text_input("Employee Name from Orgainsation")
    inquiry = st.text_area("Inquiry")

    # API Key inputs
    google_api_key = st.text_input("Google API Key", type="password")
    #serper_api_key = st.text_input("Serper API Key", type="password")

    if st.button("Submit"):
        with st.spinner("Processing..."):
            inputs = {
                "customer": customer,
                "person": person,
                "inquiry": inquiry,
            }  # Define inputs here

            result_queue = multiprocessing.Queue()
            p = multiprocessing.Process(
                target=run_crew_process,
                args=(inputs, result_queue, google_api_key),
            )
            p.start()
            result = result_queue.get()
            p.join()
            st.write(result)