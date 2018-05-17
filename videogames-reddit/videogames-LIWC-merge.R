# code to merge and label LIWC data for games project FOR VIDEO GAMES

fourpicsoneword <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (4pics1word (1000 files)).csv")
twothousandsevenscape <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (2007scape (1000 files)).csv")
twentyfortyeight <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (2048 (1000 files)).csv")
Advance_Wars <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Advance_Wars (1000 files)).csv")
aoe <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (aoe (1000 files)).csv")
aoe2 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (aoe2 (1000 files)).csv")
aoe3 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (aoe3 (1000 files)).csv")
ArenaFPS <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (ArenaFPS (1000 files)).csv")
Battlefield <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Battlefield (1000 files)).csv")
battlefield_4 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (battlefield_4 (1000 files)).csv")
Battlefield_4_CTE <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Battlefield_4_CTE (1000 files)).csv")
Bejeweled <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Bejeweled (1000 files)).csv")
beyondtwosouls <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (beyondtwosouls (1000 files)).csv")
blackops3 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (blackops3 (1000 files)).csv")
callofcthulhu <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (callofcthulhu (1000 files)).csv")
CallOfDuty <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (CallOfDuty (1000 files)).csv")
candycrushsaga <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (candycrushsaga (1000 files)).csv")
castlevania <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (castlevania (1000 files)).csv")
chess <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (chess (1000 files)).csv")
civ <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (civ (1000 files)).csv")
Clash_Royale <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Clash_Royale (1000 files)).csv")
ClashOfClans <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (ClashOfClans (1000 files)).csv")
ClashOfClansRecruit <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (ClashOfClansRecruit (1000 files)).csv")
ClashRoyale <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (ClashRoyale (1000 files)).csv")
ClashRoyaleCirclejerk <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (ClashRoyaleCirclejerk (1000 files)).csv")
COC <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (COC (1000 files)).csv")
CoDCompetitive <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (CoDCompetitive (1000 files)).csv")
commandandconquer <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (commandandconquer (1000 files)).csv")
CompetitiveHotS <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (CompetitiveHotS (1000 files)).csv")
counterstrike <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (counterstrike (1000 files)).csv")
crossword <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (crossword (1000 files)).csv")
crosswords <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (crosswords (1000 files)).csv")
csgolounge <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (csgolounge (1000 files)).csv")
dawnofwar <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (dawnofwar (1000 files)).csv")
DawnOfWarIII <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (DawnOfWarIII (1000 files)).csv")
DnD <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (DnD (1000 files)).csv")
donkeykong <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (donkeykong (1000 files)).csv")
DotA2 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (DotA2 (1000 files)).csv")
Dungeons_and_Dragons <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Dungeons_and_Dragons (1000 files)).csv")
DungeonsAndDragons <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (DungeonsAndDragons (1000 files)).csv")
DungeonWorld <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (DungeonWorld (1000 files)).csv")
EA_FIFA <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (EA_FIFA (1000 files)).csv")
ElderScrolls <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (ElderScrolls (1000 files)).csv")
Fallout <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Fallout (1000 files)).csv")
falloutsettlements <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (falloutsettlements (1000 files)).csv")
fatalframe <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (fatalframe (1000 files)).csv")
ffxiv <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (ffxiv (1000 files)).csv")
ffxivart <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (ffxivart (1000 files)).csv")
Fighters <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Fighters (1000 files)).csv")
finalfantasyx <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (finalfantasyx (1000 files)).csv")
fireemblem <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (fireemblem (1000 files)).csv")
FireEmblemHeroes <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (FireEmblemHeroes (1000 files)).csv")
FlappyBird <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (FlappyBird (1000 files)).csv")
fo4 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (fo4 (1000 files)).csv")
FoWtcg <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (FoWtcg (1000 files)).csv")
GlobalOffensive <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (GlobalOffensive (1000 files)).csv")
gmod <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (gmod (1000 files)).csv")
GrandTheftAutoV <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (GrandTheftAutoV (1000 files)).csv")
GTA <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (GTA (1000 files)).csv")
GTAV <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (GTAV (1000 files)).csv")
Guildwars2 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Guildwars2 (1000 files)).csv")
guildwars2funny <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (guildwars2funny (1000 files)).csv")
GuildWarsDyeJob <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (GuildWarsDyeJob (1000 files)).csv")
GuiltyGearXRD <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (GuiltyGearXRD (1000 files)).csv")
HaloWars <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (HaloWars (1000 files)).csv")
hearthstone <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (hearthstone (1000 files)).csv")
hearthstonecirclejerk <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (hearthstonecirclejerk (1000 files)).csv")
HearthstoneRage <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (HearthstoneRage (1000 files)).csv")
heroes3 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (heroes3 (1000 files)).csv")
heroesofthestorm <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (heroesofthestorm (1000 files)).csv")
HoMM <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (HoMM (1000 files)).csv")
iRacing <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (iRacing (1000 files)).csv")
kof <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (kof (1000 files)).csv")
leagueoflegends <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (leagueoflegends (1000 files)).csv")
learndota2 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (learndota2 (1000 files)).csv")
lifeisstrange <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (lifeisstrange (1000 files)).csv")
Mario <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Mario (1000 files)).csv")
MarioMaker <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (MarioMaker (1000 files)).csv")
Minecraft <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Minecraft (1000 files)).csv")
MinecraftBuddies <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (MinecraftBuddies (1000 files)).csv")
minecraftsuggestions <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (minecraftsuggestions (1000 files)).csv")
Minesweeper <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Minesweeper (1000 files)).csv")
minesweeperio <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (minesweeperio (1000 files)).csv")
mk9 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (mk9 (1000 files)).csv")
MMORPG <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (MMORPG (1000 files)).csv")
moba <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (moba (1000 files)).csv")
MortalKombat <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (MortalKombat (1000 files)).csv")
MortalKombatX <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (MortalKombatX (1000 files)).csv")
NexusNewbies <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (NexusNewbies (1000 files)).csv")
numenera <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (numenera (1000 files)).csv")
OldSchoolSilentHill <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (OldSchoolSilentHill (1000 files)).csv")
outlast <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (outlast (1000 files)).csv")
Overwatch <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Overwatch (1000 files)).csv")
Overwatch_Memes <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Overwatch_Memes (1000 files)).csv")
OverwatchUniversity <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (OverwatchUniversity (1000 files)).csv")
pkmntcg <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (pkmntcg (1000 files)).csv")
plants_vs_zombies <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (plants_vs_zombies (1000 files)).csv")
ptcgo <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (ptcgo (1000 files)).csv")
RealTimeStrategy <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (RealTimeStrategy (1000 files)).csv")
residentevil <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (residentevil (1000 files)).csv")
ResidentEvil7 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (ResidentEvil7 (1000 files)).csv")
rpg <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (rpg (1000 files)).csv")
runescape <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (runescape (1000 files)).csv")
scape <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (scape (1000 files)).csv")
scrabble <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (scrabble (1000 files)).csv")
sf3 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (sf3 (1000 files)).csv")
SF4 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (SF4 (1000 files)).csv")
Shadowrun <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Shadowrun (1000 files)).csv")
silenthill <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (silenthill (1000 files)).csv")
simracing <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (simracing (1000 files)).csv")
Sims3 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Sims3 (1000 files)).csv")
Sims4 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Sims4 (1000 files)).csv")
skyrim <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (skyrim (1000 files)).csv")
skyrimmods <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (skyrimmods (1000 files)).csv")
Smite <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Smite (1000 files)).csv")
SmiteLFM <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (SmiteLFM (1000 files)).csv")
smitetraining <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (smitetraining (1000 files)).csv")
solitaire <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (solitaire (1000 files)).csv")
SonicTheHedgehog <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (SonicTheHedgehog (1000 files)).csv")
starcraft <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (starcraft (1000 files)).csv")
starcraft_strategy <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (starcraft_strategy (1000 files)).csv")
StarcraftCircleJerk <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (StarcraftCircleJerk (1000 files)).csv")
StreetFighter <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (StreetFighter (1000 files)).csv")
summoners <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (summoners (1000 files)).csv")
summonerschool <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (summonerschool (1000 files)).csv")
survivalhorror <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (survivalhorror (1000 files)).csv")
TeamFortress2 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (TeamFortress2 (1000 files)).csv")
Tekken <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Tekken (1000 files)).csv")
Tekken7 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Tekken7 (1000 files)).csv")
TeraOnline <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (TeraOnline (1000 files)).csv")
Tetris <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Tetris (1000 files)).csv")
tf2 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (tf2 (1000 files)).csv")
thehedgehog <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (thehedgehog (1000 files)).csv")
thelastofus <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (thelastofus (1000 files)).csv")
thesims <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (thesims (1000 files)).csv")
TheWalkingDeadGame <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (TheWalkingDeadGame (1000 files)).csv")
TriviaCrack <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (TriviaCrack (1000 files)).csv")
TrueDoTA2 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (TrueDoTA2 (1000 files)).csv")
truetf2 <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (truetf2 (1000 files)).csv")
untildawn <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (untildawn (1000 files)).csv")
vainglorygame <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (vainglorygame (1000 files)).csv")
Vaingloryguildhall <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (Vaingloryguildhall (1000 files)).csv")
VentGlory <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (VentGlory (1000 files)).csv")
WordsWithFriends <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (WordsWithFriends (1000 files)).csv")
wow <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (wow (1000 files)).csv")
wowguilds <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (wowguilds (1000 files)).csv")
wowservers <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (wowservers (1000 files)).csv")
WWEGames <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (WWEGames (1000 files)).csv")
yugioh <- read.csv("C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC2015 Results (yugioh (1000 files)).csv")


fourpicsoneword$subreddit = "4pics1word"
twothousandsevenscape$subreddit = "2007scape"
twentyfortyeight$subreddit = "2048"
Advance_Wars$subreddit = "Advance_Wars"
aoe$subreddit = "aoe"
aoe2$subreddit = "aoe2"
aoe3$subreddit = "aoe3"
ArenaFPS$subreddit = "ArenaFPS"
Battlefield$subreddit = "Battlefield"
battlefield_4$subreddit = "battlefield_4"
Battlefield_4_CTE$subreddit = "Battlefield_4_CTE"
Bejeweled$subreddit = "Bejeweled"
beyondtwosouls$subreddit = "beyondtwosouls"
blackops3$subreddit = "blackops3"
callofcthulhu$subreddit = "callofcthulhu"
CallOfDuty$subreddit = "CallOfDuty"
candycrushsaga$subreddit = "candycrushsaga"
castlevania$subreddit = "castlevania"
chess$subreddit = "chess"
civ$subreddit = "civ"
Clash_Royale$subreddit = "Clash_Royale"
ClashOfClans$subreddit = "ClashOfClans"
ClashOfClansRecruit$subreddit = "ClashOfClansRecruit"
ClashRoyale$subreddit = "ClashRoyale"
ClashRoyaleCirclejerk$subreddit = "ClashRoyaleCirclejerk"
COC$subreddit = "COC"
CoDCompetitive$subreddit = "CoDCompetitive"
commandandconquer$subreddit = "commandandconquer"
CompetitiveHotS$subreddit = "CompetitiveHotS"
counterstrike$subreddit = "counterstrike"
crossword$subreddit = "crossword"
crosswords$subreddit = "crosswords"
csgolounge$subreddit = "csgolounge"
dawnofwar$subreddit = "dawnofwar"
DawnOfWarIII$subreddit = "DawnOfWarIII"
DnD$subreddit = "DnD"
donkeykong$subreddit = "donkeykong"
DotA2$subreddit = "DotA2"
Dungeons_and_Dragons$subreddit = "Dungeons_and_Dragons"
DungeonsAndDragons$subreddit = "DungeonsAndDragons"
DungeonWorld$subreddit = "DungeonWorld"
EA_FIFA$subreddit = "EA_FIFA"
ElderScrolls$subreddit = "ElderScrolls"
Fallout$subreddit = "Fallout"
falloutsettlements$subreddit = "falloutsettlements"
fatalframe$subreddit = "fatalframe"
ffxiv$subreddit = "ffxiv"
ffxivart$subreddit = "ffxivart"
Fighters$subreddit = "Fighters"
finalfantasyx$subreddit = "finalfantasyx"
fireemblem$subreddit = "fireemblem"
FireEmblemHeroes$subreddit = "FireEmblemHeroes"
FlappyBird$subreddit = "FlappyBird"
fo4$subreddit = "fo4"
FoWtcg$subreddit = "FoWtcg"
GlobalOffensive$subreddit = "GlobalOffensive"
gmod$subreddit = "gmod"
GrandTheftAutoV$subreddit = "GrandTheftAutoV"
GTA$subreddit = "GTA"
GTAV$subreddit = "GTAV"
Guildwars2$subreddit = "Guildwars2"
guildwars2funny$subreddit = "guildwars2funny"
GuildWarsDyeJob$subreddit = "GuildWarsDyeJob"
GuiltyGearXRD$subreddit = "GuiltyGearXRD"
HaloWars$subreddit = "HaloWars"
hearthstone$subreddit = "hearthstone"
hearthstonecirclejerk$subreddit = "hearthstonecirclejerk"
HearthstoneRage$subreddit = "HearthstoneRage"
heroes3$subreddit = "heroes3"
heroesofthestorm$subreddit = "heroesofthestorm"
HoMM$subreddit = "HoMM"
iRacing$subreddit = "iRacing"
kof$subreddit = "kof"
leagueoflegends$subreddit = "leagueoflegends"
learndota2$subreddit = "learndota2"
lifeisstrange$subreddit = "lifeisstrange"
Mario$subreddit = "Mario"
MarioMaker$subreddit = "MarioMaker"
Minecraft$subreddit = "Minecraft"
MinecraftBuddies$subreddit = "MinecraftBuddies"
minecraftsuggestions$subreddit = "minecraftsuggestions"
Minesweeper$subreddit = "Minesweeper"
minesweeperio$subreddit = "minesweeperio"
mk9$subreddit = "mk9"
MMORPG$subreddit = "MMORPG"
moba$subreddit = "moba"
MortalKombat$subreddit = "MortalKombat"
MortalKombatX$subreddit = "MortalKombatX"
NexusNewbies$subreddit = "NexusNewbies"
numenera$subreddit = "numenera"
OldSchoolSilentHill$subreddit = "OldSchoolSilentHill"
outlast$subreddit = "outlast"
Overwatch$subreddit = "Overwatch"
Overwatch_Memes$subreddit = "Overwatch_Memes"
OverwatchUniversity$subreddit = "OverwatchUniversity"
pkmntcg$subreddit = "pkmntcg"
plants_vs_zombies$subreddit = "plants_vs_zombies"
ptcgo$subreddit = "ptcgo"
RealTimeStrategy$subreddit = "RealTimeStrategy"
residentevil$subreddit = "residentevil"
ResidentEvil7$subreddit = "ResidentEvil7"
rpg$subreddit = "rpg"
runescape$subreddit = "runescape"
scape$subreddit = "scape"
scrabble$subreddit = "scrabble"
sf3$subreddit = "sf3"
SF4$subreddit = "SF4"
Shadowrun$subreddit = "Shadowrun"
silenthill$subreddit = "silenthill"
simracing$subreddit = "simracing"
Sims3$subreddit = "Sims3"
Sims4$subreddit = "Sims4"
skyrim$subreddit = "skyrim"
skyrimmods$subreddit = "skyrimmods"
Smite$subreddit = "Smite"
SmiteLFM$subreddit = "SmiteLFM"
smitetraining$subreddit = "smitetraining"
solitaire$subreddit = "solitaire"
SonicTheHedgehog$subreddit = "SonicTheHedgehog"
starcraft$subreddit = "starcraft"
starcraft_strategy$subreddit = "starcraft_strategy"
StarcraftCircleJerk$subreddit = "StarcraftCircleJerk"
StreetFighter$subreddit = "StreetFighter"
summoners$subreddit = "summoners"
summonerschool$subreddit = "summonerschool"
survivalhorror$subreddit = "survivalhorror"
TeamFortress2$subreddit = "TeamFortress2"
Tekken$subreddit = "Tekken"
Tekken7$subreddit = "Tekken7"
TeraOnline$subreddit = "TeraOnline"
Tetris$subreddit = "Tetris"
tf2$subreddit = "tf2"
thehedgehog$subreddit = "thehedgehog"
thelastofus$subreddit = "thelastofus"
thesims$subreddit = "thesims"
TheWalkingDeadGame$subreddit = "TheWalkingDeadGame"
TriviaCrack$subreddit = "TriviaCrack"
TrueDoTA2$subreddit = "TrueDoTA2"
truetf2$subreddit = "truetf2"
untildawn$subreddit = "untildawn"
vainglorygame$subreddit = "vainglorygame"
Vaingloryguildhall$subreddit = "Vaingloryguildhall"
VentGlory$subreddit = "VentGlory"
WordsWithFriends$subreddit = "WordsWithFriends"
wow$subreddit = "wow"
wowguilds$subreddit = "wowguilds"
wowservers$subreddit = "wowservers"
WWEGames$subreddit = "WWEGames"
yugioh$subreddit = "yugioh"

  

videogame_community_subset <- rbind(twothousandsevenscape, twentyfortyeight, Advance_Wars, aoe, aoe2, aoe3, ArenaFPS, Battlefield, battlefield_4, Battlefield_4_CTE, beyondtwosouls, blackops3, callofcthulhu, CallOfDuty, castlevania, chess, civ, Clash_Royale, ClashOfClans, ClashOfClansRecruit, ClashRoyale, ClashRoyaleCirclejerk, COC, CoDCompetitive, commandandconquer, CompetitiveHotS, counterstrike, crossword, crosswords, csgolounge, dawnofwar, DawnOfWarIII, DnD, donkeykong, DotA2, Dungeons_and_Dragons, DungeonsAndDragons, DungeonWorld, EA_FIFA, ElderScrolls, Fallout, falloutsettlements, fatalframe, ffxiv, ffxivart, Fighters, finalfantasyx, fireemblem, FireEmblemHeroes, FlappyBird, fo4, FoWtcg, GlobalOffensive, gmod, GrandTheftAutoV, GTA, GTAV, Guildwars2, guildwars2funny, GuildWarsDyeJob, HaloWars, hearthstone, hearthstonecirclejerk, heroes3, heroesofthestorm, HoMM, iRacing, kof, leagueoflegends, learndota2, lifeisstrange, Mario, MarioMaker, Minecraft, MinecraftBuddies, minecraftsuggestions, Minesweeper, mk9, MMORPG, moba, MortalKombat, MortalKombatX, NexusNewbies, numenera, outlast, Overwatch, Overwatch_Memes, OverwatchUniversity, pkmntcg, ptcgo, RealTimeStrategy, residentevil, ResidentEvil7, rpg, runescape, scape, scrabble, sf3, SF4, Shadowrun, silenthill, simracing, Sims3, Sims4, skyrim, skyrimmods, Smite, SmiteLFM, smitetraining, SonicTheHedgehog, starcraft, starcraft_strategy, StarcraftCircleJerk, StreetFighter, summoners, summonerschool, survivalhorror, Tekken, Tekken7, TeraOnline, Tetris, tf2, thehedgehog, thelastofus, thesims, TheWalkingDeadGame, TriviaCrack, TrueDoTA2, truetf2, untildawn, vainglorygame, Vaingloryguildhall, VentGlory, wow, wowguilds, wowservers, WWEGames, yugioh)

write.csv(videogame_community_subset, "C:/Users/mt34546/Dropbox/GradSchoolStuff(UT)/Research-Data/Reddit-VideoGames-LIWC-communities-subset/LIWC_merged_videogame_community_subset.csv")
