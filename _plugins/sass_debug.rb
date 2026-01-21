require "json"
require "fileutils"

#region agent log
def agent_debug_log(payload)
  log_path = "/Users/aurelioc/Downloads/sherpa-docs/.cursor/debug.log"
  FileUtils.mkdir_p(File.dirname(log_path))
  entry = {
    sessionId: "debug-session",
    runId: payload[:runId] || "pre-fix",
    hypothesisId: payload[:hypothesisId] || "H0",
    location: payload[:location] || "_plugins/sass_debug.rb",
    message: payload[:message] || "debug",
    data: payload[:data] || {},
    timestamp: (Time.now.to_f * 1000).to_i
  }
  File.open(log_path, "a") { |f| f.puts(entry.to_json) }
rescue StandardError
  # Swallow all errors to avoid impacting the build
end
#endregion

# Log basic site configuration relevant to Sass/theme resolution
Jekyll::Hooks.register :site, :after_init do |site|
  agent_debug_log(
    hypothesisId: "H1",
    location: "_plugins/sass_debug.rb:site_after_init",
    message: "Site config for Sass/theme debugging",
    data: {
      theme: site.config["theme"],
      sass_config: site.config["sass"],
      source: site.source,
      dest: site.dest
    }
  )
end

# Patch the SCSS converter to log load paths right before conversion
module Jekyll
  module Converters
    class Scss < Converter
      alias_method :convert_without_agent_debug, :convert

      def convert(content)
        #region agent log
        agent_debug_log(
          hypothesisId: "H2",
          location: "_plugins/sass_debug.rb:Scss#convert",
          message: "About to convert SCSS; logging sass load paths",
          data: {
            sass_config: @sass_config,
            sass_load_paths: @sass_config && @sass_config[:load_paths]
          }
        )
        #endregion

        convert_without_agent_debug(content)
      end
    end
  end
end

