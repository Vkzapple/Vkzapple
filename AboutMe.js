import aboutMe from "./aboutMe.ts";
import React from "react";
import aboutMe from "./aboutMe.ts";

const AboutMe = () => {
  return (
    <div>
      <h1>{aboutMe.name}</h1>
      <p>Location: {aboutMe.location}</p>
      <h2>Education</h2>
      <p>School: {aboutMe.education.school}</p>
      <p>Major: {aboutMe.education.major}</p>
      <p>Class: {aboutMe.education.class}</p>
      <h2>Technical Skills</h2>
      <p>Languages: {aboutMe.technicalSkills.languages.join(", ")}</p>
      <p>Frontend: {aboutMe.technicalSkills.frontend.join(", ")}</p>
      <p>Backend: {aboutMe.technicalSkills.backend.join(", ")}</p>
      <p>Databases: {aboutMe.technicalSkills.databases.join(", ")}</p>
      <p>Tools: {aboutMe.technicalSkills.tools.join(", ")}</p>
      <h2>Interests</h2>
      <p>{aboutMe.interests.join(", ")}</p>
      <h2>Current Focus</h2>
      <p>{aboutMe.currentFocus}</p>
      <h2>Hobbies</h2>
      <p>{aboutMe.hobbies.join(", ")}</p>
      <h2>Fun Fact</h2>
      <p>{aboutMe.funFact}</p>
      <h2>Life Goal</h2>
      <p>{aboutMe.getLifeGoal()}</p>
      <h2>Current Project</h2>
      <p>{aboutMe.getCurrentProject()}</p>
      <h2>Inspiration</h2>
      <p>{aboutMe.getInspiration()}</p>
    </div>
  );
};

export default AboutMe;
