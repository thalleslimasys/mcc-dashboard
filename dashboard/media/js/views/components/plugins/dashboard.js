define([
  'jquery',
  'knockout',
  'arches',
  'js-cookie',
  'templates/views/components/plugins/dashboard.htm'
], function ($, ko, arches, Cookies, DashboardTemplate) {
  return ko.components.register('dashboard', {
    viewModel: function (params) {
      const self = this;
      this.loading = ko.observable(true);
      this.records = ko.observable();
      debugger;

      this.getStatus = async function () {

        $.ajax({
          url: "/dashboard/records",
          method: "GET",
          dataType: "json",
          success: function (data) {
            debugger;
            self.resourceCount = data.resource_count;
            self.tileCount = data.tile_count;
            self.records(data.records);
            self.loading(false);
          },
          error: function (xhr, status, error) {
            debugger;
            console.error("Erro ao buscar os dados do dashboard:", error);
          }
        });
      };

      this.saveStatus = async function () {
        $.ajax({
          url: "/dashboard/records",
          method: "POST",
          dataType: "json",
          headers: {
            "X-CSRFToken": Cookies.get('csrftoken')
          },
          xhrFields: {
            withCredentials: true
          },
          success: function (data) {
            self.records(data.records);
          },
          error: function (xhr, status, error) {
            console.error("Erro ao enviar dados para o dashboard:", error);
          }
        });
      };

      this.getStatus();
    },
    template: DashboardTemplate
  });
});
