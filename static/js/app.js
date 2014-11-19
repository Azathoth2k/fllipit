var fllipit = {
    failedBefore: false,
    
    // build HTML for a single Jenkins build
    getHtmlForSingleTeam: function (team) {
        var teamData =
            "<tr><td class='numeric'>" + team.number + "</td>" +
            "<td class='text'>" + team.name + "</td>" +
            "<td class='text'>" + team.affiliation + "</td>" +
            "<td class='numeric'>" + team.round1 + "</td>" +
            "<td class='numeric'>" + team.round2 + "</td>" +
            "<td class='numeric'>" + team.round3 + "</td>" +
            "<td class='numeric'>" + team.round4 + "</td>" +
            "</tr>";
        
        return teamData;
    },

    // update the build-list HTML on the main page
    updateHtml: function (data) {
        var tableData = "<table class='table table-striped scroll'>" +
            "<thead><tr>" +
            "<th class='numeric'>Number</th>" + 
            "<th class='text'>Name</th>" + 
            "<th class='text'>Affiliation</th>" + 
            "<th class='numeric'>Round 1</th>" + 
            "<th class='numeric'>Round 2</th>" + 
            "<th class='numeric'>Round 3</th>" + 
            "<th class='numeric'>Best</th>" + 
            "</tr>" +
            "</thead><tbody>";
        $.each(data, function (i, team) {
            tableData += fllipit.getHtmlForSingleTeam(team);
        });
        tableData += "</tbody></table>";
        $("div#teams").html(tableData);
        $("#lastUpdate").html('Last updated: ' + moment().format("MMMM DD YYYY, h:mm:ss a"));
    },

    // get data from Jenkins and update the builds
    getData: function () {
        $.ajax("/api/teams?callback=?", {
            datatype: 'jsonp',
            success: function (data) {
                fllipit.updateHtml(data);
            },
            error: function (error, data, type) {
                if (!fllipit.failedBefore) {
                    alert("Failed to get data from Python server");
                    fllipit.failedBefore = true;
                    $("#lastUpdate").html('DISCONNECTED');
                }
            }
        }); 
    }
};