import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
st.title("Gear Box")

st.markdown("""<p style = 'color:red'>
            The gearbox is a mechanical device used to increase the output torque or to change the speed (RPM) of a motor. The shaft of the motor is connected to one end of the gearbox and through the internal configuration of gears of a gearbox, provides a given output torque and speed determined by the gear ratio.""",
            unsafe_allow_html = True)


with st.expander("Introdiction...  "):
    st.markdown("""<p style = 'color:yellow'> 
                The most basic definition of a gearbox is that it is a contained gear train, or a mechanical unit or component consisting of a series of integrated gears within a housing. In fact, the name itself defines what it is a box containing gears. In the most basic sense, a gearbox functions like any system of gears; it alters torque and speed between a driving device like a motor and a load.<br>    
    <br>The gears within a transmission can be one of several types, from bevel gears and spiral bevel gears to worm gears and others such as planetary gears. The gears are mounted on shafts that are carried by roller bearings and rotate about them. The gearbox is a mechanical method of transferring energy from one device to another and is used to increase the torque while reducing the speed at the same time.<br>
    <br>Gearboxes are used in many applications including machine tools, industrial equipment, conveyor belts, and virtually any rotary motion power transmission application that requires changes in torque and speed requirements.<br>
                """, unsafe_allow_html = True)


with st.expander(" How Do They Work? "):
    st.markdown("""<p style = 'color:pink'> 
    An electric or hydraulic motor is applied to one end of the gearbox, while the energy is converted into low-speed drive torque at the other end. Inside the box, the materials used have a long service life, which supports enormous strength. Can you imagine the energy it would take to tackle the wreckage of a cruise ship during the maneuver? Or that of the container crane? Or even an underground digging machine?
                """, unsafe_allow_html=True)

with st.expander("1 Helical Gearbox"):
    st.markdown("""<p style = 'color:green'> 
                Helical gears and helical Gearbox are both capable of ensuring smooth operation. The teeth of a helical gear are cut at an angle to the face of the gear. During the process, when two of the teeth begin to mesh, contact gradually begins at one end of the tooth and maintains contact as the gear rotates into a full mesh. When it comes to transmissions, helical gears are the most common gear used and even generate large amounts of thrust.
                """, unsafe_allow_html=True)
with st.expander("2 Helical Gearbox Unique Point  "):
    st.markdown("""<p style = 'color:blue'> 
                Its unique point is that it is fixed at an angle that allows more interaction in the same direction as it moves. This results in constant contact for a certain period of time. The extruder helical gearing is also used when the torsional strength is to be optimally used and also for applications with low excitement. Applications include steel, rolling mills, conveyors, elevators, oil industry.
                """, unsafe_allow_html=True)
with st.expander("3 Bevel  Helical Gearbox"):
    st.markdown("""<p style = 'color:red'> 
Do you know the critical properties of this gearbox? It is a curved set of teeth that are located on the conical surface near the edge of the device. The bevel gear train is also used to provide rotary motion between non-parallel shafts. They play their role in mining quarries, mixers, and conveyor belts.
                """, unsafe_allow_html=True)
with st.expander(" Worm Gearboxes "):
    st.markdown("""<p style = 'color:skyblue'> 
The Worm gearbox uses a large diameter worm wheel. The worm or screw engages the teeth on the periphery of the gearbox. The rotation of the worm gearbox causes the wheel to move in a similar way to this due to the screw-like movement. The setup is designed so that the setup can rotate the gear, but the gear cannot rotate the worm.<br> <br>
The angle of the screw is flat and therefore the gear is used in conveyor systems for braking or emergency stop. These gearboxes are also used in pharmaceutical and packaging machines, Bottling plant conveyors, Machines for the Food Industry.
                """, unsafe_allow_html=True)
with st.expander(" Planetary Gearbox "):
    st.markdown("""<p style = 'color:lightgreen'> 
The planetary gearbox is considered ideal and is also known for its durability, accuracy, and distinctive functionality. It is characterized by precise applications. The planetary gear extends the service life of your devices and optimizes their performance to the full.<br><br>
This gearbox is available in either a solid hollow format or with a variety of mounting options including flange, foot, or shaft. The use of this gear differs depending on the type of industry. The bottom line, however, is that the gearboxes are designed to simplify their mechanical function in various industries.
                """, unsafe_allow_html=True)


df = pd.read_csv("b30hz0.csv")
with st.expander('View Database'):
    st.dataframe(df)
st.subheader('Columns description')
col_name, col_dtype, col_display = st.columns(3)
if col_name.checkbox('Show all column names'):
    st.table(df.columns)
if col_dtype.checkbox('View column datatype'):
    st.write(list(df.dtypes))


warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Visualise Hydraulic Systems")

if st.checkbox("Show the correlation heatmap"):
    st.subheader("Correlation Heatmap")
    plt.figure(figsize=(10, 6))
    ax = sns.heatmap(df.iloc[:, 1:].corr(),
                     annot=True)  # Creating an object of seaborn axis and storing it in 'ax' variable
    bottom, top = ax.get_ylim()  # Getting the top and bottom margin limits.
    ax.set_ylim(bottom + 0.5, top - 0.5)  # Increasing the bottom and decreasing the top margins respectively.
    st.pyplot()

with st.expander("View Histograms"):
    cols = df.columns
    hist_col = st.selectbox("Select the column to view its histogram",cols)
    df[hist_col].hist()
    plt.show()
    st.pyplot()

with st.expander("View Boxplots"):
    df.boxplot(figsize = (10, 10), widths = 1)
    plt.show()
    st.pyplot()

