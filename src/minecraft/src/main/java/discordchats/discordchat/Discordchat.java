package discordchats.discordchat;

import discordchats.discordchat.network.events.messagehandler;
import discordchats.discordchat.network.events.playerjoinevent;
import discordchats.discordchat.network.connect;
import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerTickEvents;
import net.fabricmc.fabric.api.message.v1.ServerMessageEvents;
import net.fabricmc.fabric.api.networking.v1.ServerPlayConnectionEvents;
import net.minecraft.server.MinecraftServer;
import org.slf4j.LoggerFactory;
import org.slf4j.Logger;
import discordchats.discordchat.network.events.tickhandler;

public class Discordchat implements ModInitializer {
    public static final Logger LOGGER = LoggerFactory.getLogger("testmod");
    public static MinecraftServer server;

    @Override
    public void onInitialize() {
        LOGGER.info("Hello world");

        connect.main();

        ServerPlayConnectionEvents.JOIN.register((new playerjoinevent()));
        ServerTickEvents.START_SERVER_TICK.register(new tickhandler());
        ServerMessageEvents.CHAT_MESSAGE.register(new messagehandler());
    }





}
