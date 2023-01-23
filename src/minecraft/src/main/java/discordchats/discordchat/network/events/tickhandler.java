package discordchats.discordchat.network.events;

import discordchats.discordchat.Discordchat;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerTickEvents;
import net.minecraft.server.MinecraftServer;
import discordchats.discordchat.network.MakeConnection;
import net.minecraft.util.ActionResult;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.Text;

public class tickhandler implements ServerTickEvents.StartTick {
    public boolean started;
    @Override
    public void onStartTick(MinecraftServer server1) {
        if(Discordchat.server == null){
            Discordchat.server = server1;
        }
    }
}