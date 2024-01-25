# Postmortem: Website Downtime Due to Server Overload

## Issue Summary
- **Duration**: The outage lasted for 2 hours, from 3 PM to 5 PM EST on January 24, 2024.
- **Impact**: During this period, our main website was completely inaccessible, affecting approximately 75% of our users. Users experienced timeouts and error messages.
- **Root Cause**: A traffic spike overwhelmed our primary server, causing a crash due to insufficient memory and CPU resources.

## Timeline
- **3:00 PM**: Monitoring alerts indicated server downtime.
- **3:10 PM**: Initial assumption of a network issue; network team notified.
- **3:30 PM**: Investigation revealed server overload. Network issue ruled out.
- **3:45 PM**: Unusual traffic surge noticed, likely from a promotional campaign.
- **4:15 PM**: Incident escalated to senior engineers.
- **4:45 PM**: Temporary fix by rerouting traffic to backup servers.
- **5:00 PM**: Website functionality restored.

## Root Cause and Resolution
- **Cause**: Server not configured for unexpected traffic spikes, lacked scalable resources.
- **Resolution**: Traffic rerouted to backup servers; implemented auto-scaling and load balancing.

## Corrective and Preventative Measures
- **Improvements**:
  - Upgrade server infrastructure.
  - Implement robust traffic monitoring.
- **Tasks**:
  - Patch and upgrade Nginx server.
  - Add auto-scaling to cloud infrastructure.
  - Implement a load balancer.
  - Schedule regular stress tests.

---

### Engaging Elements for Postmortem

1. **Humor**: _"When our servers decided to take an unscheduled coffee break..."_
2. **Diagrams**: (Include a simple diagram of traffic spike and server response)
3. **Storytelling Approach**: Narrate the postmortem like a story from outage to resolution.

