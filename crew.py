import streamlit as st
import multiprocessing

def run_crew_process(inputs, result_queue):
    from crewai import Crew, Process
    from agents import support_agent, support_quality_assurance_agent
    from tasks import inquiry_resolution, quality_assurance_review

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
    customer = st.text_input("Customer Name")
    person = st.text_input("Support Agent")
    inquiry = st.text_area("Inquiry")

    if st.button("Submit"):
        with st.spinner("Processing..."):
            inputs = {
                "customer": customer,
                "person": person,
                "inquiry": inquiry,
            }  # Define inputs here

            result_queue = multiprocessing.Queue()
            p = multiprocessing.Process(target=run_crew_process, args=(inputs, result_queue))
            p.start()
            result = result_queue.get()
            p.join()
            st.write(result)