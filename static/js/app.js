var fllipit = {
    failedBefore: false,
    
    // build HTML for a single Jenkins build
    getHtmlForSingleTeam: function (team) {
        var teamData =
            "<tr><td>" + team.number + "</td>" +
            "<td>" + team.name + "</td>" +
            "<td>" + team.affiliation + "</td>" +
            "<td>" + team.round1 + "</td>" +
            "<td>" + team.round2 + "</td>" +
            "<td>" + team.round3 + "</td>" +
            "</tr>";
        
        return teamData;
    },

    // update the build-list HTML on the main page
    updateHtml: function (data) {
        var tableData = "<table class='table table-striped'><tr>" + 
            "<th>Number</th>" + 
            "<th>Name</th>" + 
            "<th>Affiliation</th>" + 
            "<th>Round 1</th>" + 
            "<th>Round 2</th>" + 
            "<th>Round 3</th>" + 
            "</tr>";
        $.each(data, function (i, team) {
            tableData += fllipit.getHtmlForSingleTeam(team);
        });
        tableData += "</table>";
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