"use strict";
/**
 * @file AboutMe.ts
 * @description Personal profile and current activity
 * @last-updated 2024
 */
Object.defineProperty(exports, "__esModule", { value: true });
var aboutMe = {
    name: "Evelly Khanzania Putri",
    location: "Jakarta, Indonesia",
    education: {
        school: "SMK NEGERI 1 JAKARTA",
        major: "Software Engineering",
        class: "X RPL",
    },
    technicalSkills: {
        languages: ["JavaScript", "TypeScript", "Java", "C#", "PHP", "HTML", "CSS"],
        frontend: ["React.js", "Tailwind CSS", "Bootstrap"],
        backend: ["Node.js", "Express.js"],
        databases: ["MySQL", "MongoDB"],
        tools: ["Git", "GitHub", "VS Code", "Postman"],
    },
    interests: [
        "Frontend Development",
        "Backend Development",
        "Web Design",
        "UI/UX Design",
        "Mobile Development",
    ],
    currentFocus: "Building full-stack web applications",
    hobbies: ["Coding", "Reading Tech Blogs", "Learning New Technologies"],
    funFact: "I love turning coffee into code ☕",
    getLifeGoal: function () {
        return "To become a successful software engineer and create impactful applications";
    },
    getCurrentProject: function () {
        return "Working on exciting full-stack projects";
    },
    getInspiration: function () {
        return "Technology's potential to change the world";
    },
};
// Export for portfolio use
exports.default = aboutMe;
