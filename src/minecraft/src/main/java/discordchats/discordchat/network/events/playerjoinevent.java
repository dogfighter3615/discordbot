package discordchats.discordchat.network.events;

import discordchats.discordchat.Discordchat;
import discordchats.discordchat.util.sendchat;
import net.fabricmc.fabric.api.networking.v1.PacketSender;
import net.fabricmc.fabric.api.networking.v1.ServerPlayConnectionEvents;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.network.ServerPlayNetworkHandler;

public class playerjoinevent implements ServerPlayConnectionEvents.Join {

    @Override
    public void onPlayReady(ServerPlayNetworkHandler handler, PacketSender sender, MinecraftServer server) {
        Discordchat.LOGGER.info("<");
        Discordchat.LOGGER.info(server.toString());
        Discordchat.LOGGER.info("/>");
    }
}
