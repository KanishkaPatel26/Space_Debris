import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_explore_page():


    st.image("debris.jpg", width=700)
    st.title("SpaceTrace")
    st.markdown("Space debris detection made easier!")

    # Objectives section
    st.header("Our mission:")
    st.markdown("""   
        - Predict the Radar Cross Section (RCS) size of debris objects.
        - Detect orbit type of debris by classifying it.
    """)

    # How it works section
    st.header("FAQs")
    st.markdown("""       
        1. What is orbital debris?\n
            Orbital debris is any human-made object in orbit about the Earth that no longer serves any useful purpose.
        2. What are examples of orbital debris?\n
            Derelict spacecraft and upper stages of launch vehicles, carriers for multiple payloads, debris intentionally released during spacecraft separation from its launch vehicle or during mission operations, debris created as a result of spacecraft or upper stage explosions or collisions, solid rocket motor effluents, and tiny flecks of paint released by thermal stress or small particle impacts.
        3. How much orbital debris is currently in Earth orbit?\n
            More than 25,000 objects larger than 10 cm are known to exist. The estimated population of particles between 1 and 10 cm in diameter is approximately 500,000. The number of particles larger than 1 mm exceeds 100 million. As of January 2022, the amount of material orbiting the Earth exceeded 9,000 metric tons.
        4. How fast is orbital debris traveling?\n
            In low Earth orbit (below 2,000 km), orbital debris circles the Earth at speeds of about 7 to 8 km/s. However, the average impact speed of orbital debris with another space object is approximately 10 km/s, and can be up to about 15 km/s, which is more than 10 times the speed of a bullet. Consequently, collisions with even a small piece of debris will involve considerable energy.
        5. With so many objects in Earth orbit, what is the likely outcome of collisions between orbital debris and operational spacecraft?\n
            Operational spacecraft are struck by very small, sub-millimeter-sized orbital debris (and micrometeoroids) routinely with little or no effect. Millimeter-sized orbital debris represents the highest penetration risk to most robotic missions operating in low Earth orbit. The probability of two large objects (> 10 cm in diameter) accidentally colliding is very low. The worst such incident occurred on 10 February 2009 when an operational U.S. Iridium satellite and a derelict Russian Cosmos satellite collided.
    """
    )
    # Simulated data for space debris counts in different orbits
    orbit_data = {
        'Low Earth Orbit (LEO)': 1500,
        'Geostationary Orbit (GEO)': 800,
        'Medium Earth Orbit (MEO)': 600,
        'Polar Orbit': 400,
        'Elliptical Orbit': 300
    }

    # Calculate total debris count across all orbits
    total_debris = sum(orbit_data.values())

    # Calculate percentage of debris in each orbit
    orbit_labels = list(orbit_data.keys())
    debris_counts = list(orbit_data.values())
    debris_percentages = [count / total_debris * 100 for count in debris_counts]

    # Find the index of the orbit with the highest percentage of debris
    most_dangerous_index = np.argmax(debris_percentages)

    # Plotting the pie chart with adjusted layout and styling
    fig, ax = plt.subplots(figsize=(8, 8))
    explode = [0.1 if i == most_dangerous_index else 0 for i in range(len(orbit_labels))]
    ax.pie(debris_counts, labels=orbit_labels, autopct='%1.1f%%', startangle=90, explode=explode,
           labeldistance=1.1, pctdistance=0.85)  # Adjust label and percentage distances
    # ax.set_title('Space Debris Distribution by Orbit')
    plt.tight_layout()

    # Display the pie chart using Streamlit
    st.header('Space Debris Distribution by Orbit')
    st.pyplot(fig)  # Display the Matplotlib figure using st.pyplot()

def main():
    # Set page title and icon
    st.set_page_config(page_title="Space Debris Explorer", page_icon="🛰")
    
    # Display the explore page
    show_explore_page()

if __name__ == "__main__":
    main()



