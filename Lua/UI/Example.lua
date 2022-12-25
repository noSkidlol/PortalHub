
local Library = loadstring(game:HttpGet(('https://raw.githubusercontent.com/noSkidlol/PortalHub/main/Lua/UI/Portal-Lib.lua')))()
local Win = Library:Window({
    Name = "Hoho Hub",
    Desc = "V1",
    Theme = "PortalTheme"
})

Win:Section("Example Section")

Win:Button("Example Button",function()
	Library:Notification({
        Title = "Portal UI Library",
        Text = "Example Notification!",
        Duration = 6,
        Theme = "PortalTheme"
    }) 
end)

Win:Toggle("Example Toggle", function(Vals)
    Library:Notification({
        Title = "Portal UI Library",
        Text = "Value : "..tostring(Vals),
        Duration = 6,
        Theme = "PortalTheme"
    }) 
end)

Win:Box("Example TextBox", function(Vals)
    Library:Notification({
        Title = "Portal UI Library",
        Text = Vals,
        Duration = 6,
        Theme = "PortalTheme"
    }) 
end)

Win:Label("Example Label")

Win:Init()
