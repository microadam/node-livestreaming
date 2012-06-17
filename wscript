def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.env.prepend_value('CXXFLAGS', ['-D__STDC_CONSTANT_MACROS'])
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')

  conf.check(header_name='libavformat/avformat.h', mandatory=True)
  conf.check(lib='avutil', uselib_store='LIBAVUTIL')
  conf.check(lib='avformat', uselib_store='LIBAVFORMAT')
  conf.check(lib='avcodec', uselib_store='LIBAVCODEC')


def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.cxxflags = ["-g", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall"]
  obj.target = "livestreaming"
  obj.source = ["src/binding.cpp", "src/segmentercontext.cpp"]
  obj.uselib = ['LIBAVUTIL', 'LIBAVFORMAT', 'LIBAVCODEC']
