# ServerDeck — Base MVP Project Outline

**Version:** v0.1.0 Testing MVP  
**Initial Game Support:** Minecraft Java Edition — Vanilla  
**Initial Platform:** Windows 11  
**Primary Goal:** Prove that ServerDeck can install, configure, run, monitor, back up, and manage a Minecraft Java server without requiring the user to manually work with command-line tools or server files.

---

## 1. Product Vision

ServerDeck is intended to become a one-stop desktop application for people who want to self-host dedicated game servers without dealing with the usual setup and maintenance work.

The long-term product may support many games, modded servers, remote management, automated updates, advanced backups, notifications, and other server-management features.

The **base MVP is intentionally much smaller**.

For the first testing version, ServerDeck only needs to prove one thing:

> A normal Windows user can use ServerDeck to create and operate a vanilla Minecraft Java server with minimal technical knowledge.

---

## 2. MVP Success Criteria

The MVP is successful when a tester can:

1. Install or launch ServerDeck on a Windows PC.
2. Create a new Minecraft Java server through ServerDeck.
3. Configure basic server settings.
4. Accept the Minecraft EULA through an explicit ServerDeck workflow.
5. Start the Minecraft server.
6. Connect to the server from another Minecraft Java client on the local network.
7. Stop and restart the server safely.
8. See whether the server is online or offline.
9. View basic server output/logs.
10. Create a backup of the Minecraft world.
11. Restore a previous backup.
12. Close and reopen ServerDeck without losing the configured server.
13. Recover from a Minecraft server crash or unexpected process exit.
14. Complete the above without manually editing Minecraft server files.

If these tasks work reliably on machines other than the developer's PC, the MVP has done its job.

---

# 3. MVP Scope

## Included

### 3.1 Minecraft Java — Vanilla Only

The first version supports:

- Minecraft Java Edition dedicated server
- One Minecraft server instance
- Vanilla server only
- No Forge
- No Fabric
- No NeoForge
- No Bukkit / Spigot / Paper
- No mods
- No plugins

The internal design should avoid making future multi-game support unnecessarily difficult, but the MVP should **not** attempt to solve those future problems yet.

---

## 3.2 Server Creation

The user can create a Minecraft server from ServerDeck.

Minimum setup fields:

- Server name
- Minecraft version
- Server folder/location
- Maximum players
- Difficulty
- Game mode
- Online mode
- PvP enabled/disabled
- Whitelist enabled/disabled
- MOTD / server description
- Server port
- Allocated RAM

ServerDeck should generate or update the required Minecraft configuration instead of requiring manual file editing.

---

## 3.3 Java Runtime Check

Before attempting to run Minecraft, ServerDeck should determine whether a compatible Java runtime is available.

The MVP should:

- Detect Java
- Determine the installed Java version when possible
- Tell the user if Java is missing or incompatible
- Prevent starting the server when requirements are not satisfied
- Provide clear instructions for resolving the problem

Automatic Java installation may be considered later.

It is **not required** for the base MVP.

---

## 3.4 Minecraft Server Installation

ServerDeck should handle the Minecraft server installation workflow.

ServerDeck should:

- Obtain the selected supported server version
- Create the required server directory
- Place the required server files in that directory
- Generate initial configuration
- Track the installed Minecraft version
- Detect whether the server has already been installed

The user should not need to manually download or move the Minecraft server JAR.

---

## 3.5 EULA Workflow

Minecraft requires acceptance of its EULA before the server can run.

ServerDeck must **not silently accept the EULA for the user**.

The application should:

1. Explain that Minecraft requires EULA acceptance.
2. Provide access to the applicable EULA.
3. Require the user to explicitly confirm acceptance.
4. Only then update the server's EULA configuration.

---

# 4. Core Server Controls

The main server screen should provide:

- **Start Server**
- **Stop Server**
- **Restart Server**

The application should know the current server state:

- Offline
- Starting
- Online
- Stopping
- Crashed / unexpectedly stopped

ServerDeck should prevent invalid actions such as:

- Starting an already-running server
- Starting multiple copies of the same server process
- Restarting while no server exists
- Deleting or replacing active server files while the server is running

---

# 5. Server Status

The primary dashboard should show at minimum:

- Server name
- Minecraft version
- Online / offline state
- Process ID when running
- Current RAM usage
- Current CPU usage
- Server uptime

Nice-to-have if reasonably easy during MVP development:

- Current player count
- Maximum player count

Player count is **not required** for MVP completion if it significantly expands scope.

---

# 6. Console and Logs

The user should be able to view Minecraft server output from within ServerDeck.

Minimum requirements:

- Display server stdout/stderr
- Keep the display readable
- Show new lines while the server is running
- Preserve or expose the Minecraft server log file
- Allow the user to identify obvious startup failures

Optional for MVP:

- Search logs
- Filter warnings/errors
- Export logs
- Syntax highlighting
- Log analysis

These are future improvements.

---

# 7. Safe Shutdown

ServerDeck should attempt to stop Minecraft cleanly rather than simply killing the process.

Expected shutdown flow:

1. Request the Minecraft server to save.
2. Request a normal shutdown.
3. Wait for the process to terminate.
4. Only force terminate if the server fails to close within a defined timeout.

The program should avoid corrupting the world whenever possible.

---

# 8. Crash Detection

ServerDeck should distinguish between:

- User-requested shutdown
- Normal application shutdown
- Unexpected Minecraft server process exit

If the server exits unexpectedly:

- Mark the server as crashed/offline
- Record the event
- Preserve relevant logs
- Tell the user that the server stopped unexpectedly

### Automatic Restart

For the base MVP, automatic restart may be a simple toggle:

**Automatically restart after a crash**

If enabled:

1. Detect unexpected exit.
2. Wait a short cooldown period.
3. Attempt restart.
4. Limit repeated restart attempts to avoid an endless crash loop.
5. Notify the user if automatic recovery fails.

---

# 9. Backups

Backups are a core MVP feature.

The user should be able to click:

**Create Backup**

ServerDeck should:

1. Ensure the world is in a safe state.
2. Copy the required world data.
3. Store the backup separately from the active server.
4. Timestamp the backup.
5. Display available backups.

Suggested backup naming:

`2026-09-15_10-30-00`

or equivalent internal metadata.

---

## 9.1 Backup Restore

The user should be able to select a backup and restore it.

Restore flow:

1. Confirm the user wants to restore.
2. Require the server to be stopped.
3. Preserve or replace the current world safely.
4. Restore the selected backup.
5. Report success or failure.

ServerDeck should avoid silently deleting the active world.

A safety backup before restoration is strongly recommended.

---

## 9.2 Automatic Backups

For the testing MVP, support a basic interval setting such as:

- Disabled
- Every 30 minutes
- Every hour
- Every 2 hours
- Every 4 hours
- Every 6 hours

Advanced retention rules are postponed.

For MVP testing, a simple maximum-backup count is sufficient.

Example:

> Keep the newest 10 backups.

---

# 10. Configuration Editing

The user should be able to change supported Minecraft settings without manually opening `server.properties`.

Initial editable fields:

- MOTD
- Difficulty
- Game mode
- Max players
- PvP
- Online mode
- Whitelist
- Server port
- View distance, if included
- Simulation distance, if included

ServerDeck must validate values before writing them.

Where practical, settings that require a restart should clearly indicate that a restart is needed.

---

# 11. Whitelist Management

If whitelist support is included in the first testing build, the user should be able to:

- Enable/disable whitelist mode
- Add a player
- Remove a player
- View currently whitelisted players

If implementing reliable player identity lookup significantly delays the MVP, whitelist management may be reduced to enabling/disabling the setting for v0.1.

---

# 12. Local Network Guidance

ServerDeck's first goal is **local/LAN hosting**.

The application should show enough information for another computer on the same network to connect.

Useful information:

- Local IP address
- Minecraft port
- Example connection address

Example:

`192.168.1.50:25565`

ServerDeck should clearly distinguish:

- Local/LAN access
- Internet/public access

---

# 13. Port Forwarding

Automatic router configuration is **not part of the base MVP**.

ServerDeck may include a simple help page explaining:

- Why port forwarding may be required
- Which Minecraft port is being used
- That router interfaces vary
- Basic firewall considerations
- Security warnings related to exposing a server publicly

Future ServerDeck versions may include more advanced networking assistance.

For v0.1, the app should **not pretend it can configure every router automatically**.

---

# 14. Windows Firewall

If practical and safe, ServerDeck may detect whether Windows Firewall is likely blocking the Minecraft server.

The MVP may:

- Explain that firewall permission is required
- Tell the user which executable/port needs access
- Direct the user through the necessary Windows prompt

Automatic firewall-rule management is optional for the testing MVP.

---

# 15. Persistent Application State

ServerDeck must remember its server configuration between launches.

At minimum persist:

- Server name
- Installation path
- Minecraft version
- RAM allocation
- Server settings
- Backup location
- Backup configuration
- Crash restart preference
- Last known server state where appropriate

SQLite is a good candidate for structured ServerDeck data.

Minecraft's own configuration files remain the authoritative source for Minecraft-specific server configuration where appropriate.

---

# 16. Error Handling

The MVP should prioritize understandable errors.

Bad:

> Process returned exit code 1.

Better:

> Minecraft could not start. ServerDeck could not find a compatible Java installation.

The application should handle expected failures such as:

- Java missing
- Wrong Java version
- Download failure
- Server JAR missing
- Invalid installation folder
- Port already in use
- Insufficient RAM
- Insufficient disk space
- Server crash
- Backup failure
- Restore failure
- Permission denied
- Corrupt or inaccessible files

Technical details should still be available in logs for troubleshooting.

---

# 17. Application Logging

ServerDeck itself should maintain logs separate from Minecraft's logs.

ServerDeck logs should record important events such as:

- Application startup
- Server installation
- Configuration changes
- Server start
- Server stop
- Crash detection
- Automatic restart
- Backup creation
- Backup restoration
- Download failures
- File errors
- Unexpected exceptions

Logs will be essential once external testers begin using the application.

---

# 18. Basic UI

The MVP does not need a highly polished interface.

It does need to be clear and usable.

Suggested screens:

## Home / Dashboard

Displays:

- Server name
- Status
- Minecraft version
- Uptime
- CPU
- RAM
- Start
- Stop
- Restart

## Server Setup

Used for first-time creation.

## Settings

Minecraft configuration and ServerDeck options.

## Backups

List, create, restore, and delete backups.

## Console / Logs

Live Minecraft console output and access to logs.

## Help / Network

LAN address, port information, and basic public-server guidance.

---

# 19. Proposed Internal Architecture

Even though v0.1 supports only Minecraft, avoid placing all logic directly in the GUI.

Suggested conceptual separation:

```text
ServerDeck
│
├── UI
│
├── Application / Service Layer
│
├── Minecraft Adapter
│   ├── Install
│   ├── Start / Stop
│   ├── Configuration
│   ├── Logs
│   └── World Locations
│
├── Process Manager
├── Backup Manager
├── Download Manager
├── Monitoring
├── Scheduler
├── Persistence
└── Logging
```

The exact Python modules should be designed as development begins.

The important rule is:

> The GUI should request actions. It should not contain the actual server-management logic.

This will make it much easier to add additional games later.

---

# 20. Future Game Adapter Goal

Minecraft-specific behavior should eventually sit behind an interface that could support other games.

Conceptually, every future game adapter will need to answer questions like:

- How is this server installed?
- How is it updated?
- How is it started?
- How is it stopped?
- Where is its configuration?
- Where are save files located?
- How are backups created?
- How can ServerDeck determine whether it is healthy?
- What runtime/dependencies does it require?

Do **not** build a complete generic adapter framework before the Minecraft MVP works.

The first Minecraft implementation should teach us what the real abstraction needs to be.

---

# 21. Explicitly Out of Scope for v0.1

The following features are **not part of the base testing MVP**:

- Minecraft Bedrock
- Multiple Minecraft server instances
- Multiple games
- Modded Minecraft
- Fabric
- Forge
- NeoForge
- Paper / Spigot / Bukkit
- Modrinth integration
- CurseForge integration
- Automatic dependency resolution
- Modpack creation
- Plugin marketplace
- Remote web dashboard
- Mobile application
- User accounts
- Cloud accounts
- Cloud backups
- Discord notifications
- Email notifications
- SMS notifications
- Server marketplace
- Paid subscriptions
- Licensing / activation system
- Linux support
- macOS support
- Docker
- Automatic router configuration
- UPnP/NAT automation
- Remote console over the internet
- Advanced performance graphs
- Multiple-server orchestration
- Public ServerDeck API

These are deliberately postponed.

---

# 22. Development Phases

## Phase 0 — Research and Technical Spike

Goal:

Prove Python can reliably control a Minecraft server on Windows before building the application.

Tasks:

- Understand Minecraft Java server startup requirements
- Test Java detection
- Test server download workflow
- Launch Minecraft server from Python
- Capture stdout/stderr
- Send or perform graceful shutdown
- Detect process exit
- Identify world/config/log locations

**Exit condition:**  
A temporary Python prototype can install or launch a test Minecraft server and stop it safely.

---

## Phase 1 — Core Server Engine

Build the non-GUI Minecraft management layer.

Required capabilities:

- Install server
- Validate installation
- Start server
- Stop server
- Restart server
- Detect process state
- Capture output
- Detect unexpected exit

**Exit condition:**  
Core logic works repeatedly without relying on the GUI.

---

## Phase 2 — Configuration and Persistence

Add:

- Server settings model
- ServerDeck settings
- SQLite persistence
- `server.properties` read/write support
- Input validation

**Exit condition:**  
ServerDeck can be closed and reopened without losing the configured server.

---

## Phase 3 — Backup System

Add:

- Manual backup
- Backup listing
- Backup restore
- Basic automatic backups
- Backup count limit

**Exit condition:**  
A world can be backed up, changed, restored, and verified.

---

## Phase 4 — Monitoring and Recovery

Add:

- CPU usage
- RAM usage
- Uptime
- Crash detection
- Optional automatic restart
- Restart-attempt limit

**Exit condition:**  
Force-closing the Minecraft process is detected and ServerDeck responds correctly.

---

## Phase 5 — GUI

Build the first usable Windows interface around the tested backend.

Screens:

- Setup
- Dashboard
- Settings
- Backups
- Console
- Help/network

**Exit condition:**  
Normal server management no longer requires direct command-line interaction.

---

## Phase 6 — Packaging

Create a distributable Windows testing build.

Goals:

- User does not need the source code
- User does not need a Python development environment
- ServerDeck has a predictable data/config location
- Application logs can be located easily for bug reports

An installer can be added here or shortly after initial internal testing.

---

## Phase 7 — Internal Dogfooding

Use ServerDeck as the real Minecraft server manager.

Test it during actual gameplay.

Look specifically for:

- Crashes
- World corruption
- Failed backups
- Bad shutdown behavior
- Settings that do not apply correctly
- RAM problems
- Port conflicts
- Confusing UI
- Missing recovery paths

Use it long enough to discover problems that scripted tests will not reveal.

---

## Phase 8 — Closed External Testing

Give ServerDeck to a small number of testers.

Ideal initial testers:

- Friends
- Other Windows gamers
- People who have hosted Minecraft before
- At least one person who has never hosted a server before

The inexperienced tester is especially important.

If they can set up a server without needing personal help from the developer, the application is doing its job.

---

# 23. Testing Strategy

The project should include automated tests for logic that can be tested safely without launching a real Minecraft server.

Examples:

- Settings validation
- Configuration parsing
- Configuration writing
- Backup naming
- Backup retention
- Path handling
- Database operations
- Process-state handling where mockable
- Crash-restart limits
- Version metadata handling

Integration tests should cover interactions with the filesystem and process management where practical.

Manual testing will still be required for:

- Real Minecraft startup
- Real Minecraft shutdown
- Client connectivity
- Real server crashes
- Actual world saves
- Backup restore verification
- Firewall behavior
- Different Windows machines

---

# 24. Tester Feedback Goals

The first public/Reddit testing build is **not primarily intended to make money**.

Its purpose is to answer:

### Setup

- Could you install it?
- Did ServerDeck correctly detect what was missing?
- Were you able to create a server without reading an outside tutorial?

### Usability

- Was anything confusing?
- Did you need to manually edit files?
- Did you need to open PowerShell or Command Prompt?
- Did you understand how friends could connect?

### Reliability

- Did the server stay running?
- Did backups work?
- Did restart work?
- Did ServerDeck recover after a crash?
- Did anything damage or lose the Minecraft world?

### Product

- Would you use this instead of manually hosting a Minecraft server?
- What feature did you expect that was missing?
- What other games would you want supported?
- Would you install a future version?
- Would you pay for advanced features?

---

# 25. MVP Definition of Done

ServerDeck v0.1 is considered ready for external testing when:

- [ ] Fresh Windows machine can run ServerDeck
- [ ] Java requirement is correctly checked
- [ ] User can create a vanilla Minecraft Java server
- [ ] Minecraft server files are handled by ServerDeck
- [ ] EULA acceptance is explicit
- [ ] Server starts
- [ ] Server stops gracefully
- [ ] Server restarts
- [ ] Online/offline state is accurate
- [ ] Server console output is visible
- [ ] Basic CPU usage is visible
- [ ] Basic RAM usage is visible
- [ ] Uptime is visible
- [ ] Configuration changes work
- [ ] Server settings survive application restart
- [ ] Manual backup works
- [ ] Backup restore works
- [ ] Automatic backup works
- [ ] Unexpected Minecraft process exit is detected
- [ ] Optional automatic crash restart works
- [ ] LAN connection instructions are available
- [ ] ServerDeck produces useful diagnostic logs
- [ ] App survives common expected errors without crashing
- [ ] At least one non-developer machine has successfully hosted a playable Minecraft world

---

# 26. What Comes Immediately After MVP

Do not begin these until the testing MVP is stable.

Likely next steps:

1. Fix tester-reported issues.
2. Improve onboarding.
3. Add multiple Minecraft server instances.
4. Add Minecraft server variants such as Paper.
5. Add the first mod loader.
6. Explore Modrinth integration.
7. Add better network diagnostics.
8. Build the first non-Minecraft game adapter.
9. Determine which features belong in Free vs. paid versions.
10. Begin building a public product website.

---

# 27. Long-Term Direction

Possible future ServerDeck ecosystem:

```text
ServerDeck Desktop
        │
        ├── Minecraft
        ├── Rust
        ├── Valheim
        ├── Palworld
        ├── ARK
        ├── DayZ
        ├── Arma
        ├── Project Zomboid
        ├── 7 Days to Die
        └── Other supported dedicated servers

                ↓

        Optional ServerDeck Cloud

                ↓

        Remote Management
        Monitoring
        Notifications
        Cloud Backups
        Multi-machine Management
```

The MVP should establish the reliable local-server foundation that all of this can eventually sit on.

---

# 28. Guiding Principle

For every MVP feature, ask:

> Does this make creating or operating the first Minecraft server materially easier or safer?

If the answer is **no**, it probably belongs after v0.1.

ServerDeck v0.1 does not need to be impressive because it has many features.

It needs to be impressive because the small number of things it does **actually work**.
