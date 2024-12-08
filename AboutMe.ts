interface CurrentActivity {
  status: string;
  timestamp: string;
}

interface Education {
  school: string;
  major: string;
  class: string;
}

interface TechnicalSkills {
  languages: string[];
  frontend: string[];
  backend: string[];
  databases: string[];
  tools: string[];
}

interface DeveloperProfile {
  readonly name: string;
  location: string;
  education: Education;
  technicalSkills: TechnicalSkills;
  interests: string[];
  currentFocus: string;
  hobbies: string[];
  funFact: string;
  currentActivity: CurrentActivity;
  getLifeGoal(): string;
  getCurrentProject(): string;
  getInspiration(): string;
}

const aboutMe: DeveloperProfile = {
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
  currentActivity: {
    status: "Working on exciting full-stack projects 🚀",
    timestamp: new Date().toISOString(),
  },
  getLifeGoal: function (): string {
    return "To become a successful software engineer and create impactful applications";
  },
  getCurrentProject: function (): string {
    return "Working on exciting full-stack projects";
  },
  getInspiration: function (): string {
    return "Technology's potential to change the world";
  },
};

export default aboutMe;
